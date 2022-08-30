from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'first_name',  'last_name', 'avatar']


class CreatePostForm(ModelForm):
    all_images = forms.ImageField(label=u'Photos', widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Post
        fields = ['description', 'tags']
