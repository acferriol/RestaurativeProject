from django.contrib import admin
from django.urls import path
from repo.views import DocumentsListView

urlpatterns = [
    path('work', DocumentsListView.as_view(),name="work"),
]