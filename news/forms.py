from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        #fields = ['title', 'full_text', 'date']
        fields = ['title', 'full_text', 'genre', 'language', 'date', 'author', 'location']     #fieldlist

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
            "genre": TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
            "language": TextInput(attrs={'class': 'form-control', 'placeholder': 'Language'}),
            "date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Date', 'type': 'date'}),
            "author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            "location": TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }