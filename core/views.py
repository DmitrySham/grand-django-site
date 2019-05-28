from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, Http404
from .models import GrandSmeta

# Create your views here.


def index(request):
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
