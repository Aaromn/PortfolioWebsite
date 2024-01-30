from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os

def index(request):
    return render(request, 'portfolio/index.html')

def about_page(request):
    return render(request, 'portfolio/about.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def bounce(request):
    return HttpResponseRedirect('https://aaromnn.pythonanywhere.com')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        send_mail(
            f'Message from {name} ({email})',
            message,
            'aaronespana777@gmail.com',  # Your email address
            ['aaronespana812@gmail.com'],  # Recipient email address
            fail_silently=False,
        )

        # Redirect to a thank-you page or the same page
        return HttpResponseRedirect('https://aaromnn.pythonanywhere.com')  # Change the URL as needed

    return render(request, 'portfolio/resume.html')  # Render the same template for GET requests
