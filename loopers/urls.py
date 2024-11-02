from django.urls import path
from loopers import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('about-loopers-it/', views.about_us, name='about_us')
]