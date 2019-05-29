from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from .models import *

# Create your views here.


def one_c_list(request):
    objects = OneC.objects.filter(is_active=True)

    return render(request, 'app/one-c.html', locals())


def one_c_single(request, id):
    try:
        one_c_object = OneC.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/one-c-single.html', locals())


def online_cashbox_list(request):
    objects = OnlineCashbox.objects.filter(is_active=True)
    partners = OnlineCashBoxPartner.objects.filter(is_active=True)

    return render(request, 'app/online-cashbox.html', locals())


def online_cashbox_single(request, id):
    try:
        online_cashbox = OnlineCashbox.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/online-cashbox-single.html', locals())


def electronic_signature_list(request):
    electronic_signature = ElectronicSignature.objects.filter(is_active=True)

    return render(request, 'app/electronic-sign-list.html', locals())


def electronic_signature_single(request, slug):
    try:
        electronic_signature = ElectronicSignature.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return Http404

    return render(request, 'app/electronic-sign-single.html', locals())
