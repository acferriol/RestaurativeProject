from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    about = models.TextField()
    img = models.ImageField(upload_to="media/profiles" ,null=True,blank=True)
    twitter = models.CharField(max_length=50,blank=True,null=True)
    facebook = models.CharField(max_length=50,blank=True,null=True)
    instagram = models.CharField(max_length=50,blank=True,null=True)
    linkedin = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name
    