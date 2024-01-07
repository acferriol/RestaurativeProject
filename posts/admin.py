from django.contrib import admin
from posts.models import Post,ImagePost
from posts.forms import PostForm

# Register your models here.
class ImagePostAdmin(admin.TabularInline):
    model = ImagePost

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [ImagePostAdmin]

admin.site.register(Post,PostAdmin)
admin.site.register(ImagePost)