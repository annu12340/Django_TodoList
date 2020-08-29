from django import forms
from .models import Blog


class TodoForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'