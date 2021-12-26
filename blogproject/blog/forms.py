from django import forms

from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ["title", "body"]