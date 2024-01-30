from django.urls import path

from .views import send_message
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('send-message/', send_message, name='send_message'),
]
