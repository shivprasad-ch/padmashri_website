from django import forms
from .models import Nominee, ContactRequest

# -------------------------
# 👤 Nominee Data Form
# -------------------------
class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee
        fields = [
            'full_name',
            'tagline',
            'profile_photo',
            'bio',
            'field_of_work',
            'impact_numbers'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'tagline': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short tagline (e.g., A Life of Service)'
            }),
            'profile_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter biography...'
            }),
            'field_of_work': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Field of work (e.g., Education, Social Work)'
            }),
            'impact_numbers': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'e.g., 10,000+ lives impacted'
            }),
        }

# -------------------------
# ✉️ Contact Form
# -------------------------
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message',
                'rows': 4
            }),
        }