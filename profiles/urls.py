from django.contrib import admin
from django.urls import path
from profiles.views import ProfilesListView

urlpatterns = [
    path('team', ProfilesListView.as_view(),name="team"),
]