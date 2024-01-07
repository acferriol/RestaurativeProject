from django.contrib import admin
from django.urls import path
from posts.views import PostListView

urlpatterns = [
    path('main', PostListView.as_view(),name="main"),
]