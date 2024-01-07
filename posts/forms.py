from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post

        fields = [
            'title',
            'about',
            'participants',
            'date',
            'place',
        ]

        labels = {
            'title':"Title",
            'about':"About this",
            'participants':'Participants',
            'date':"Date",
            'place':"Place",
        }

        widgets = {
            'title': forms.TextInput(),
            'about': forms.Textarea(),
            'participants': forms.SelectMultiple(),
            'date': forms.DateInput(attrs={'class':'form-control','type':'date'},format="%Y-%m-%d"),
            'place': forms.TextInput(),
        }

        