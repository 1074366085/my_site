from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="posts-detail-page"),  # /posts/my-first-post
    path("add", views.add_post, name="add-post")
]
