from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Blog, Comments

User = get_user_model()



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
