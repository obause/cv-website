from . import views
from django.urls import path


urlpatterns = [
    # path("", views.HomePageView.as_view(), name="blog"),
    path("", views.AllPostsView.as_view(), name="blog"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),  # slug: checks for slug format
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
