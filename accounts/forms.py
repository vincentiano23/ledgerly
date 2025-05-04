from django import forms
from .models import LedgerEntry

class LedgerEntryForm(forms.ModelForm):
    class Meta:
        model = LedgerEntry
        fields = ['account', 'description', 'date', 'debit', 'credit']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'debit': forms.NumberInput(attrs={'class': 'form-control'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control'}),
        }
