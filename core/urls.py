from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("resume", views.resume, name="resume"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.ContactView.as_view(), name="contact")
]
