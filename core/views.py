import json
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


from .models import GrandSmeta, Slider, Contacts, AdminEmails, Feedback, PrivacyPolicy, PromoFormField, PromoVisitor
from .utils import get_client_ip


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
                phone=feedback_form.cleaned_data['phone'],
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


def privacy_policy(request):
    _privacy_policy = PrivacyPolicy.objects.first()

    return render(request, 'app/privacy-policy.html', {'privacy_policy': _privacy_policy})


def save_promo_user(request):
    try:
        data: dict = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Не удалось разпознать данные'}, status=400)

    post_id = data.pop('post')

    try:
        Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'Пост не найден или уже удален!'}, status=400)

    values: 'list' = data.pop('values')
    form_data = {}

    if len(values) == 0:
        return JsonResponse({'message': 'Проверьте правильность заплненных данных'}, status=400)

    for item in values:
        try:
            field = PromoFormField.objects.get(id=item['field_id'])
        except PromoFormField.DoesNotExist:
            return JsonResponse({'message': 'Поле [#%s] не найдено!' % item['field_id']}, status=400)
        form_data[field.field_placeholder] = item['value']

    options = dict(
        post_id=post_id,
        form_data=json.dumps(form_data),
        ip=get_client_ip(request)
    )

    if not request.user.is_anonymous:
        options['user_id'] = request.user.id

    visitor = PromoVisitor.objects.create(**options)

    return JsonResponse({})
