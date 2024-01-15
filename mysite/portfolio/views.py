from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import os

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about_page(request): 
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)
    return render(request, 'portfolio/about.html')

def resume(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def skills(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def projects(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def contact(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def portfolio(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def bounce(request):
    return HttpResponseRedirect('https://aaromnn.pythonanywhere.com/portfolio')


