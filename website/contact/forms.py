from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['message']
        labels = {
            'message': 'Deine Nachricht'
        }
