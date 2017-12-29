from django.urls import path
from . import views

app_name = 'coursesapp'

urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='course_list'),
]
