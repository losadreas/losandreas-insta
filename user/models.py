import django_resized.forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500, blank=True)
    avatar = ResizedImageField(size=[1000, None], upload_to='account/avatars/%y/%m/%d', null=True, blank=True)
    token = models.CharField(max_length=124, blank=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Post(models.Model):
    description = models.CharField(_("description"), max_length=150, blank=True)
    date_posted = models.DateTimeField(_("date posted"), default=timezone.now)
    tags = models.CharField(_("tags"), max_length=150, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_post')
    quantity_likes = models.PositiveIntegerField(default=0)


# fix for incorrect settings initialization in django-images
django_resized.forms.DEFAULT_NORMALIZE_ROTATION = False


class Image(models.Model):
    images = ResizedImageField(size=[1000, None], upload_to='posts/%y/%m/%d')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE, related_name='all_images')
