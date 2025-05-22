from django import forms
from .models import PC, Composant

class PCForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = ['nom']

class ComposantForm(forms.ModelForm):
    class Meta:
        model = Composant
        fields = ['nom', 'type']
