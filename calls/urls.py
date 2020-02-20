from django.urls import path
from calls import views

urlpatterns = [
    path('ajax/call/request/', views.call_request, name='calls_request')
]
