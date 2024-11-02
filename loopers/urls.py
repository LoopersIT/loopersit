from django.urls import path
from loopers import views

urlpatterns = [
    path('', views.home_page, name='homepage')
]