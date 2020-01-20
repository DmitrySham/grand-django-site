from django.urls import path
from checkouts import views

urlpatterns = [
    path('ajax/checkout/request', views.checkout_request, name='checkout_request')
]
