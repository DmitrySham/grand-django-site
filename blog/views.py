from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def blog_list(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'app/blog-list.html', locals())


def blog_single(request, slug):
    try:
        post = Post.objects.get(slug=slug, is_active=True)
    except ObjectDoesNotExist:
        raise Http404

    recent_posts = Post.objects.filter(is_active=True).exclude(id=post.id).order_by('-created_at')[:3]
    return render(request, 'app/blog-single.html', locals())
