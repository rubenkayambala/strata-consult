from django import forms
from .models import Achat


class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['plateforme', 'lien', 'adresse']
        widgets = {
            'plateforme': forms.Select(attrs={'class': 'form-control p-3'}),
            'lien': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Inserez le lien de l'article"}),
            'adresse': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Inserez l'adresse de livraison"}),
        }
        