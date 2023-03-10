from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm


def get_date(post):
    return post.get('date')


class HomePageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# def start_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/blog_posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all_posts.html", {
#         "all_posts": all_posts
#     })


class PostDetailView(View):
    def is_stored_for_later(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            return post_id in stored_posts
        return False

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_for_later(request, post.id)
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_for_later(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tags'] = self.object.tags.all()
    #     context['comment_form'] = CommentForm()
    #     return context

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     # post = next(post for post in posts_content if post['slug'] == slug)
#     return render(request, "blog/post-detail.html", {
#         "post": post,
#         "tags": post.tags.all()
#     })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts", [])

        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts", [])

        post_id = int(request.POST.get("post_id"))

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/read-later")
