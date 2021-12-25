from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("about", views.about, name='About'),
    path("services", views.services, name='Services'),
    path("contact", views.contact, name='Contact'),
    # path("submit", views.contact, name="contact"),

]
