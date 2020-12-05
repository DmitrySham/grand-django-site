from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from core.models import PromoFormBuilder, PromoVisitor
from core.utils import get_client_ip

from .models import Post

# Create your views here.


def blog_list(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'app/blog-list.html', locals())


def blog_single(request, slug):
    try:
        post = Post.objects.get(slug=slug, is_active=True)
    except ObjectDoesNotExist:
        raise Http404

    form: PromoFormBuilder = PromoFormBuilder.objects.first()

    recent_posts = Post.objects.filter(is_active=True).exclude(id=post.id).order_by('-created_at')[:3]

    has_promo = post.is_promo
    ip = get_client_ip(request)
    previous_visits = PromoVisitor.objects.filter(ip=ip, post_id=post.id)

    if previous_visits.exists():
        has_promo = False

    return render(request, 'app/blog-single.html', locals())
