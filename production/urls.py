from django.urls import path
from production import views as production_views


urlpatterns = [
    # path('list/', production_views.one_c_list, name='one_c_list'),
    path('1c/<int:id>/', production_views.one_c_single_old, name='one_c_single_old'),
    # path('<str:slug>/', production_views.one_c_single, name='one_c_single'),

    # path('online-cashbox/', production_views.online_cashbox_list, name='online_cashbox_list'),
    path('online-cashbox/<int:id>', production_views.online_cashbox_single_old, name='online_cashbox_single_old'),
    path('online-cashbox/<str:slug>', production_views.online_cashbox_single, name='online_cashbox_single'),

    path('electronic-signature/', production_views.electronic_signature_list, name='electronic_signature_list'),
    path('electronic-signature/<str:slug>/', production_views.electronic_signature_single, name='electronic_signature_single')
]
