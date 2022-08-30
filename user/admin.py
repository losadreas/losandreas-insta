from django.contrib import admin

# Register your models here.
from user.models import User, Post, Image

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Image)
