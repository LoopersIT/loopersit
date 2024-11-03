from django.urls import path
from . import views


urlpatterns = [
    path('', views.career_list, name='career_list')
]