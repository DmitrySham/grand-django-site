from django.shortcuts import render
from .models import *

# Create your views here.


def one_c_list(request):
    objects = OneC.objects.all()

    return render(request, 'app/one-c.html', locals())


def one_c_single(request, id):
    one_c_object = OneC.objects.get(id=id)

    return render(request, 'app/one-c-single.html', locals())
