from django.shortcuts import render
from django.template import RequestContext

from .models import Contact, Interests


def home(request):
    # contact = Contact.objects.first()

    return render(request, "core/main.html")


def about(request):
    context = {"interest_rows": []}
    all_interests = Interests.objects.all()
    # row = 0
    row_content = []
    for i, interest in enumerate(all_interests):
        print(i, interest)
        row_content.append(interest)
        if i % 2 == 1:
            context['interest_rows'].append(row_content)
            row_content = []
    if len(row_content) > 0:
        context['interest_rows'].append(row_content)
    print(context)
    return render(request, "core/about.html", context)


def resume(request):
    return render(request, "core/resume.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
