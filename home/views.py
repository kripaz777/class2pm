from django.shortcuts import render
from .models import Contact, ContactInformation,Testonomial


# Create your views here.
def home(request):
    view = {}
    view['reviews'] = Testonomial.objects.all()
    return render(request,'index.html',view)

def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    view = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject= subject,
            message = message
        )
        data.save()
        view['success'] = "The message is submitted."

    view['info'] = ContactInformation.objects.all()
    return render(request, 'contact.html',view)