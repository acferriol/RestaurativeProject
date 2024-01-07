from django.shortcuts import render
from profiles.models import Author
from django.views.generic import ListView

# Create your views here.
class ProfilesListView(ListView):
    model = Author
    template_name = 'team.html'

    def get_queryset(self):
        return self.model.objects.all()