from django.shortcuts import render
from repo.models import Document
from django.views.generic import ListView

# Create your views here.
class DocumentsListView(ListView):
    model = Document
    template_name = 'repo.html'

    def get_queryset(self):
        return self.model.objects.all()

