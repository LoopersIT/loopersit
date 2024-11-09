from django.urls import path
from . import views


urlpatterns = [
        path('contact-loopers-it/', views.ContactView.as_view(), name='contact_us'),
        path('contact-success/', views.contact_success, name='contact_success'),
]