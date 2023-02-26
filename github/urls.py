from . import views
from django.urls import path


urlpatterns = [
    path("github-test", views.github_test, name="github-test")
]
