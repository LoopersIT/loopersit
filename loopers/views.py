from django.shortcuts import render, get_object_or_404
from .models import Service



def home_page(request):
    services = Service.objects.all()
    return render(request, 'loopers/home_page.html', {'services':services})

def service(request):
    services = Service.objects.all()
    return render(request, 'loopers/service.html', {'active': 'service', 'services':services})

def sub_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'loopers/sub_service.html', {'active': 'service', 'service':service})


def about_us(request):
    return render(request, 'loopers/about_us.html', {'active':'about'})

def contact_us(request):
    return render(request, 'loopers/contact_us.html', {'active': 'contact'})

def reviews(request):
    return render(request, 'loopers/reviews.html', {'active':'review'})