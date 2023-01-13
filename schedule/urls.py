from django.urls import path
from schedule import views as schedule_views


urlpatterns = [
    path('courses/', schedule_views.course_list, name='list'),
    # path('courses/<str:slug>/', schedule_views.course_single, name='single'),
    path('educators/', schedule_views.EducatorsView.as_view(), name='educators_list'),
    path('educators/<str:slug>/', schedule_views.EducatorsSingleView.as_view(), name='educators_detail'),
    path('', schedule_views.schedule, name='base_view')
]
