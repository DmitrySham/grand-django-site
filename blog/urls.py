from blog import views as blog_views
from django.urls import path


urlpatterns = [
    path('posts/', blog_views.blog_list, name='list'),
    path('posts/<str:slug>/', blog_views.blog_single, name='single'),
]
