from django.shortcuts import render


def main(request):
    return render(request, "core/main.html")


def about(request):
    return render(request, "core/about.html")


def resume(request):
    return render(request, "core/resume.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
