from django import forms

from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "subject": "Subject",
            "message": "Message"
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'email': forms.EmailInput(attrs={"class": 'form-control'}),
            'subject': forms.TextInput(attrs={"class": 'form-control'}),
            'message': forms.Textarea(attrs={"class": 'form-control'}),
        }
