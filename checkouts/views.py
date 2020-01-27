import threading

import django
from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_POST

from core.models import AdminEmails
from schedule.utils import send_email_notification
from .forms import CheckoutForm
from .models import Checkout


def get_model(model_name):
    if model_name == 'onec':
        return apps.get_model(app_label='production',
                              model_name=model_name)
    elif model_name == 'grandsmeta':
        return apps.get_model(app_label='core',
                              model_name=model_name)
    return None


@require_POST
def checkout_request(request):
    model_name = request.POST.get('model_name', None)
    model_id = request.POST.get('model_id', None)

    if not model_id or not model_name:
        return HttpResponse('', status=400)

    model = get_model(model_name)
    obj = get_object_or_404(model, id=model_id)

    form = CheckoutForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)

        if model_name == 'onec':
            instance.one_c = obj
        elif model_name == 'grandsmeta':
            instance.grand_smeta = obj
        instance.save()

        template = loader.get_template('app/email/checkout.html')

        content_type = ContentType.objects.get_for_model(Checkout)
        protocol = 'https://' if request.is_secure() else 'http://'
        context = dict(
            name=instance.name,
            email=instance.email,
            object=obj,
            message=instance.message,
            created_at=instance.created_at,
            link=protocol + request.get_host() + reverse(
                'admin:%s_%s_change' % (content_type.app_label, content_type.model), args=(instance.id,)),
            # admin_link=f"{Site.objects.get(id=settings.SITE_ID).domain}/admin/",
            admin_link=protocol + request.get_host() + "/admin/",
        )
        mail_response = template.render(request=request, context=context)

        admin_emails = [item.email for item in AdminEmails.objects.filter(is_active=True)]
        thread = threading.Thread(
            target=send_email_notification,
            args=(
                'Заказы',
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
