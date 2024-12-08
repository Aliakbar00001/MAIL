from django import forms
from django.forms import CharField


class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
