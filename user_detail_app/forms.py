from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user_detail_app.models import *


class Subscriptionform(forms.ModelForm):

    class Meta:
        model=user_details
        # fields='__all__'
        fields=['email',]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email', 'required': 'true'}),          
        }