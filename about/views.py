from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from config.settings.pro import EMAIL_HOST_USER
from .forms import ContactForm
from .models import FAQ

# Create your views here.

def about_us(request):
    return render(request, 'about/about_us.html', {'active':'about'})

class ContactView(View):
    def get(self, request):
        contact_form = ContactForm()
        faqs = FAQ.objects.all()
        return render(request, 'about/contact_us.html', {
            'active': 'contact', 
            'contact_form':contact_form,
            'faqs':faqs})
    
    def post(self, request):
        contact_form = ContactForm(request.POST)
        faqs = FAQ.objects.all()
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            body = {
                'name': contact_form.cleaned_data['name'],
                'email': contact_form.cleaned_data['email'],
                'message': contact_form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, EMAIL_HOST_USER, ['loopersit@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Inavalid header found')
            return redirect('contact_success')
        return render(request, 'about/contact_us.html', {
            'active': 'contact', 
            'contact_form':contact_form,
            'faqs':faqs})



def contact_success(request):
    return render(request, 'success.html', {'active': 'contact'})