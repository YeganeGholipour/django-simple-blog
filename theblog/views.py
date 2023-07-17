from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.db.models import Count

# def home(request):
# return render(request, "home.html", {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # ordering = ["-id"]
    ordering = ["-post_date"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = "__all__"
    # fields = ("title", "body")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    form_class = EditForm
    # fields = ["title", "title_tag", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class AddCAtegoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"
    # fields = ("title", "body")


def CategoryView(requests, cats):
    category_post = Post.objects.filter(category=cats.replace("-", " "))
    return render(
        requests,
        "categories.html",
        {"cats": cats.title().replace("-", " "), "category_posts": category_post},
    )


class AllCategoryView(ListView):
    model = Post
    template_name = "all_category.html"
    queryset = (
        Post.objects.values("category")
        .annotate(total=Count("category"))
        .order_by("category")
    )
