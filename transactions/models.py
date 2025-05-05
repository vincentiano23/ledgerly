from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    """
    Represents an accounting ledger account.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('JE', 'Journal Entry'),
        ('CP', 'Cash Payment'),
        ('CR', 'Cash Receipt'),
        ('BP', 'Bank Payment'),
        ('BR', 'Bank Receipt'),
    ]

    transaction_type = models.CharField(max_length=2, choices=TRANSACTION_TYPES)
    date = models.DateField()
    description = models.TextField(blank=True)
    debit_account = models.ForeignKey(Account, related_name='debit_transactions', on_delete=models.PROTECT)
    credit_account = models.ForeignKey(Account, related_name='credit_transactions', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.date} - {self.amount}"
