from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
import os

def index(request):
    send_mail("The Subject", "Hi, I am the message", "aaronespana777@gmail.com", ["aaronespana812@gmail.com", "aaronespana777@gmail.com"])
    return HttpResponse("Hello, world. You're at the polls index.")

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