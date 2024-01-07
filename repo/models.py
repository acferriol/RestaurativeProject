from django.db import models
from profiles.models import Author
import os
# Create your models here.
class Document(models.Model):
    participants =  models.ManyToManyField(Author)
    name = models.CharField(max_length=50,blank=True,null=True)
    tags = models.CharField(max_length=40,blank=True,null=True)
    file = models.FileField(upload_to="media/docs",blank=True,null=True)

    def extension(self):
        name,extension = os.path.splitext(self.file.name)
        return extension