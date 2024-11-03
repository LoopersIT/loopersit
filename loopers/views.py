from django.shortcuts import render



def home_page(request):
    return render(request, 'loopers/home_page.html', {})

def about_us(request):
    return render(request, 'loopers/about_us.html', {'active':'about'})

def contact_us(request):
    return render(request, 'loopers/contact_us.html', {'active': 'contact'})