from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'sender','subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Type your name'}),
            'sender': forms.TextInput(attrs={'placeholder': 'Type your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.TextInput(attrs={'placeholder': 'Message'}),

        }