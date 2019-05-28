import threading

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from core.models import AdminEmails
from .models import Course, ApplyRequest
from .forms import ApplyRequestForm
from .utils import send_email_notification

# Create your views here.


def course_list(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'app/shedule-object-list.html', locals())


@ensure_csrf_cookie
def course_single(request, slug):
    try:
        course = Course.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    apply_form = ApplyRequestForm(initial={'course': course.get_actual_date_action()})

    if request.POST:
        if not course.get_actual_date_action():
            return JsonResponse(dict(success=False, message='Нет актуального расписания. Просим прощения за доставленные неудобства!'))

        if int(course.get_actual_date_action().get_free_place_count()) <= 0:
            return JsonResponse(dict(success=False, message='Не удалось записаться! Не осталось свободных мест!'))

        apply_form = ApplyRequestForm(request.POST, initial=dict(course=course.get_actual_date_action()))
        if apply_form.is_valid():
            apply_credentials = dict(
                name=apply_form.cleaned_data['name'],
                email=apply_form.cleaned_data['email'],
                phone=apply_form.cleaned_data['phone'],
                education=apply_form.cleaned_data['education'],
                message=apply_form.cleaned_data['message'],
                course=apply_form.cleaned_data['course']
            )

            apply_request = ApplyRequest.objects.create(**apply_credentials)

            template = loader.get_template('app/email/apply-request.html')
            apply_credentials['course'] = apply_request.course.course.title
            apply_credentials['created_at'] = apply_request.created_at

            protocol = 'https://' if request.is_secure() else 'http://'
            site_url = protocol + request.get_host()

            content_type = ContentType.objects.get_for_model(apply_request.__class__)
            apply_credentials['link'] = site_url + reverse('admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(apply_request.id,))

            mail_response = template.render(context=apply_credentials, request=request)

            emails = [item.email for item in AdminEmails.objects.filter(is_active=True)]

            thread = threading.Thread(
                target=send_email_notification,
                args=(
                    'Заявка | Grand',
                    mail_response,
                    [emails]
                )
            )
            thread.start()
            return JsonResponse(dict(success=True, message='Вы успешно записались на курс! Мы свяжемся с вами для уточнения деталей. Спасибо, что выбираете нас!'))

        return JsonResponse(dict(success=False, message=str(apply_form.errors)))

    return render(request, 'app/schedule-object-single.html', locals())


def schedule(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'app/schedule.html', locals())
