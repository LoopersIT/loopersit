from django.urls import path
from loopers import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('services/', views.service, name='service_page'),
    path('service/<slug:slug>/', views.sub_service, name='sub_service'),
    path('reviews/', views.reviews, name='reviews'),
]