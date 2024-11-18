from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'date_of_birth', 'password1', 'password2']
