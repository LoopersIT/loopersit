from django.shortcuts import render
from .models import Service



def home_page(request):
    return render(request, 'loopers/home_page.html', {})

def service(request):
    services = Service.objects.all()
    return render(request, 'loopers/service.html', {'active': 'service', 'services':services})

def sub_service(request):
    return render(request, 'loopers/sub_service.html', {'active': 'service'})


def about_us(request):
    return render(request, 'loopers/about_us.html', {'active':'about'})

def contact_us(request):
    return render(request, 'loopers/contact_us.html', {'active': 'contact'})

def reviews(request):
    return render(request, 'loopers/reviews.html', {'active':'review'})