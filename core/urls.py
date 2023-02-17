from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home-page"),
    path("about", views.about, name="about-page"),
    path("resume", views.resume, name="resume-page"),
    path("portfolio", views.portfolio, name="portfolio-page"),
    path("blog", views.blog, name="blog-page"),
    path("contact", views.contact, name="contact-page")
]
