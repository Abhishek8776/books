from django import forms
from .models import BookModal

class BookForm(forms.ModelForm):
  # title = forms.CharField(
  #   label='Book Title',
  #   max_length=200,
  #   widget=forms.TextInput(attrs={'placeholder': 'Enter the book title'}),
  # )
  # author = forms.CharField(
  #   label='Author',
  #   max_length=100,
  #   widget=forms.TextInput(attrs={'placeholder': 'Enter the author'}),
  # )
  class Meta:
    model = BookModal
    fields = ['title', 'author']