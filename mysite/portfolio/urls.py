"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #Pre-defined paths
    path("polls/", include("polls.urls")),

    #Paths defined by me
    path("resume/", views.resume),
    path('about/', views.about_page, name='about'),
    path("skills/", views.skills),
    path("projects/", views.projects),
    path("contact/", views.contact),
    path("", views.index),
]
