# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book  # assuming you have a Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # replace with real fields
