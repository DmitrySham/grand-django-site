from django.urls import path
from production import views as production_views


urlpatterns = [
    path('1c/list/', production_views.one_c_list, name='one_c_list'),
    path('1c/<int:id>/', production_views.one_c_single, name='one_c_single'),

    path('online-cashbox/', production_views.online_cashbox_list, name='online_cashbox_list'),
    path('online-cashbox/<int:id>', production_views.online_cashbox_single, name='online_cashbox_single'),
]
