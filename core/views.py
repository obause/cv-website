from django.shortcuts import render
from django.template import RequestContext

from .models import Contact


def home(request):
    # contact = Contact.objects.first()

    return render(request, "core/main.html")


def about(request):
    contact = Contact.objects.first()
    print(f"Age: {contact.age()}")
    return render(request, "core/about.html")


def resume(request):
    return render(request, "core/resume.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
