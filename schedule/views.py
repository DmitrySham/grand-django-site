from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from core.models import FAQ, StudentsReviews
from .models import Course, License, Educators, SubscriptionPlans

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

    advantages = course.advantages.filter(is_active=True)
    subscription_plans = course.subscription_plans.filter(is_active=True)
    reviews = StudentsReviews.objects.filter(is_active=True)
    faq_items = FAQ.objects.filter(is_active=True)
    siblings = course.siblings.all()[:8]

    # apply_form = ApplyRequestForm(initial={'course': course.get_actual_date_action()})

    # if request.POST:
    #     if not course.get_actual_date_action():
    #         return JsonResponse(dict(success=False, message='Нет актуального расписания. Просим прощения за доставленные неудобства!'))
    #
    #     if int(course.get_actual_date_action().get_free_place_count()) <= 0:
    #         return JsonResponse(dict(success=False, message='Не удалось записаться! Не осталось свободных мест!'))
    #
    #     apply_form = ApplyRequestForm(request.POST, initial=dict(course=course.get_actual_date_action()))
    #     # print(request.POST)
    #     if apply_form.is_valid():
    #         # print(apply_form.cleaned_data['education'])
    #         apply_credentials = dict(
    #             first_name=apply_form.cleaned_data['first_name'],
    #             last_name=apply_form.cleaned_data['last_name'],
    #             middle_name=apply_form.cleaned_data['middle_name'],
    #             email=apply_form.cleaned_data['email'],
    #             phone=apply_form.cleaned_data['phone'],
    #             education=apply_form.cleaned_data['education'],
    #             message=apply_form.cleaned_data['message'],
    #             course=apply_form.cleaned_data['course']
    #         )
    #
    #         apply_request = ApplyRequest.objects.create(**apply_credentials)
    #
    #         template = loader.get_template('app/email/apply-request.html')
    #         apply_credentials['course'] = apply_request.course.course.title
    #         apply_credentials['created_at'] = apply_request.created_at
    #
    #         protocol = 'https://' if request.is_secure() else 'http://'
    #         site_url = protocol + request.get_host()
    #
    #         content_type = ContentType.objects.get_for_model(apply_request.__class__)
    #         apply_credentials['link'] = site_url + reverse('admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(apply_request.id,))
    #
    #         mail_response = template.render(context=apply_credentials, request=request)
    #
    #         emails = [item.email for item in AdminEmails.objects.filter(is_active=True)]
    #
    #         thread = threading.Thread(
    #             target=send_email_notification,
    #             args=(
    #                 'Заявка | Grand',
    #                 mail_response,
    #                 [emails]
    #             )
    #         )
    #         thread.start()
    #         return JsonResponse(dict(success=True, message='Вы успешно записались на курс! Мы свяжемся с вами для уточнения деталей. Спасибо, что выбираете нас!'))
    #
    #     return JsonResponse(dict(success=False, message=str(apply_form.errors)))

    return render(request, 'app/schedule-object-single-new.html', locals())


@ensure_csrf_cookie
def course_full_description(request, slug):
    try:
        course = Course.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/schedule-object-full-description.html', locals())


@ensure_csrf_cookie
def course_roadmap(request, slug):
    try:
        course = Course.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/schedule-object-roadmap.html', locals())


def schedule(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'app/schedule.html', locals())


class LicensesView(generic.TemplateView):
    template_name = 'app/licenses.html'

    def get_context_data(self, **kwargs):
        context = super(LicensesView, self).get_context_data(**kwargs)
        context.update({
            'licenses': License.objects.filter(is_active=True)
        })
        return context


class EducatorsView(generic.TemplateView):
    template_name = 'app/educators.html'
    model = Educators

    def get_queryset(self):
        return self.model.objects.filter(is_active=True).order_by('order_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'educators': self.get_queryset()
        })
        return context


class EducatorsSingleView(generic.DetailView):
    template_name = 'app/educators-single.html'
    model = Educators
    pk_url_kwarg = 'id'
    context_object_name = 'educator'
