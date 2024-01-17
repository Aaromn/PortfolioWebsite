from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
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


