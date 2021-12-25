from os import name
from django.http.response import HttpResponse
from datetime import date, datetime
from Home.models import Contact
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    # return HttpResponse("This is Contactpage")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent!')

    return render(request,'contact.html')