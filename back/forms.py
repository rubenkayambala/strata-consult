from django import forms
from .models import Achat


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['username', 'full_name', 'email', 'phone', 'gender', 'birthday', 'profile', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Nom d'utilisateur"}),
            'full_name': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Nom complet"}),
            'email': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Email'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control p-3', 'placeholder': 'Date de naissance'}),
            'phone': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Téléphone'}),
            'gender': forms.Select(attrs={'class': 'form-control p-3'}),
            'profile': forms.Select(attrs={'class': 'form-control p-3'}),
            'password': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Mot de passe'}),
        }
        