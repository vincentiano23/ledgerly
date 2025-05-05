from django import forms
from .models import Transaction, Account

class TransactionForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        required=False
    )
    amount = forms.DecimalField(
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
    )
    transaction_type = forms.ChoiceField(
        choices=Transaction.TRANSACTION_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    debit_account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    credit_account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'date', 'description', 'debit_account', 'credit_account', 'amount']
