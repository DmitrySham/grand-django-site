from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.


def one_c_list(request):
    objects = OneC.objects.filter(is_active=True)

    return render(request, 'app/one-c.html', locals())


def one_c_single_old(request, id):
    try:
        one_c_object = OneC.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('production:one_c_single', kwargs={'slug': one_c_object.slug}))


def one_c_single(request, slug):
    try:
        one_c_object = OneC.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'app/one-c-single.html', locals())


def online_cashbox_list(request):
    categories = OnlineCashboxCategory.objects.all()
    prepared_categories = list()

    for category in categories:
        prepared_categories.append(dict(
            category=category,
            objects=OnlineCashbox.objects.filter(is_active=True, category_id=category.id)
        ))

    others = OnlineCashbox.objects.filter(is_active=True, category__isnull=True)

    if others.count() > 0:
        prepared_categories.append(dict(
            category=dict(title='Другие'),
            objects=others
        ))

    # objects =
    partners = OnlineCashBoxPartner.objects.filter(is_active=True)

    return render(request, 'app/online-cashbox.html', locals())


def online_cashbox_single_old(request, id):
    try:
        online_cashbox = OnlineCashbox.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('production:online_cashbox_single', kwargs={'slug': online_cashbox.slug}))


def online_cashbox_single(request, slug):
    try:
        online_cashbox = OnlineCashbox.objects.get(slug=slug)
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
