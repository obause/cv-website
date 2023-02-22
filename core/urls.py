from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("resume", views.resume, name="resume"),
    path("portfolio", views.portfolio, name="portfolio"),
    # path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("test", views.test, name="test")
]
