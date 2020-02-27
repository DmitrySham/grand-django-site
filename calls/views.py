import threading

from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_POST

from calls.forms import CallForm
from calls.models import Call
from core.models import AdminEmails
from schedule.utils import send_email_notification


@require_POST
def call_request(request):
    form = CallForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        template = loader.get_template('app/email/calls.html')

        content_type = ContentType.objects.get_for_model(Call)
        protocol = 'https://' if request.is_secure() else 'http://'
        context = dict(
            name=instance.name,
            phone=instance.phone,
            object=instance,
            message=instance.message,
            created_at=instance.created_at,
            link=protocol + request.get_host() + reverse(
                'admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(instance.id,)),
            admin_link=protocol + request.get_host() + "/admin/",
        )
        mail_response = template.render(request=request, context=context)

        admin_emails = [item.email for item in AdminEmails.objects.filter(is_active=True)]
        thread = threading.Thread(
            target=send_email_notification,
            args=(
                'Звонки',
                mail_response,
                admin_emails
            )
        )
        thread.start()
        data = {
            'message': 'Ваша заявка принята! Мы свяжемся с вами в скором времени'
        }

        return JsonResponse(data)
    return JsonResponse(dict(data=str(form.errors)), status=400)
