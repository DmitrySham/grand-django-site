from django.urls import path
from schedule import views as schedule_views


urlpatterns = [
    path('courses/', schedule_views.course_list, name='list'),
    path('courses/<str:slug>/', schedule_views.course_single, name='single'),
    path('', schedule_views.schedule, name='base_view')
]
