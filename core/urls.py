from django.urls import path
from core import views as core_views


urlpatterns = [
    path('grand-smeta/', core_views.grand_smeta_list, name='grand_smeta_list'),
    path('grand-smeta/<str:slug>/', core_views.grand_smeta_single, name='grand_smeta_single'),
    path('contacts/', core_views.contacts, name='contacts')
]
