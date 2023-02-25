from . import views
from django.urls import path


urlpatterns = [
    # path("", views.HomePageView.as_view(), name="blog"),
    path("", views.resume_pdf, name="resume-pdf")
]
