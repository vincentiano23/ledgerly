from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('AS', 'Asset'),
        ('LI', 'Liability'),
        ('EQ', 'Equity'),
        ('RE', 'Revenue'),
        ('EX', 'Expense'),
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES)

    def __str__(self):
        return f"{self.code} - {self.name}"

class LedgerEntry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date = models.DateField()
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.date} | {self.account} | Dr {self.debit} | Cr {self.credit}"
