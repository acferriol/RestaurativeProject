from django.db import models
from profiles.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30,blank=True,null=True)
    about = models.TextField(default="Hola")
    participants = models.ManyToManyField(Author,related_name='authors')
    date = models.DateField()
    place = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self) -> str:
        return "Post"+super().__str__()[-2:-1]

class ImagePost(models.Model):
    image = models.ImageField(upload_to="media/posts" ,null=True,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")