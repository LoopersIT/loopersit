from django.shortcuts import render



def home_page(request):
    return render(request, 'loopers/home_page.html', {})