import threading

from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, Http404
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

from blog.models import Post
from core.forms import FeedbackForm
from schedule.utils import send_email_notification
from .models import GrandSmeta, Slider, Contacts, AdminEmails, Feedback


# Create your views here.


def index(request):
    posts = Post.objects.filter(is_active=True)
    slides = Slider.objects.filter(is_active=True)
    return render(request, 'app/index.html', locals())


def grand_smeta_list(request):
    grand_smeta = GrandSmeta.objects.filter(is_active=True)
    return render(request, 'app/grand-smeta-list.html', locals())


def grand_smeta_single(request, slug):
    try:
        grand_smeta = GrandSmeta.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/grand-smeta-single.html', locals())


@ensure_csrf_cookie
def contacts(request):
    contacts_object = Contacts.objects.first()

    feedback_form = FeedbackForm()

    if request.POST:
        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            feedback_object = feedback_form.save()

            template = loader.get_template('app/email/feedback.html')

            content_type = ContentType.objects.get_for_model(Feedback)
            protocol = 'https://' if request.is_secure() else 'http://'
            context = dict(
                name=feedback_form.cleaned_data['name'],
                email=feedback_form.cleaned_data['email'],
                subject=feedback_form.cleaned_data['subject'],
                message=feedback_form.cleaned_data['message'],
                created_at=feedback_object.created_at,
                link=protocol + request.get_host() + reverse('admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(feedback_object.id,))
            )

            mail_response = template.render(request=request, context=context)

            admin_emails = [item.email for item in AdminEmails.objects.filter(is_active=True)]

            thread = threading.Thread(
                target=send_email_notification,
                args=(
                    'Обратная связь',
                    mail_response,
                    admin_emails
                )
            )
            thread.start()
            return JsonResponse(dict(success=True, message='Ваше письмо отправлено! Мы свяжемся с вами в скором времени'))

        return JsonResponse(dict(success=False, message=str(feedback_form.errors)))

    return render(request, 'app/contacts.html', locals())


def handler404(request, *args, **argv):
    response = render(request, 'not_found.html', locals())
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'internal_error.html', locals())
    response.status_code = 500
    return response
