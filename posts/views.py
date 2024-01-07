from django.shortcuts import render
from posts.models import Post
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'main.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-date')