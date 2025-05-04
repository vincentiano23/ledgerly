from django.contrib import admin
from .models import Account, LedgerEntry

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type')
    search_fields = ('name', 'code')

@admin.register(LedgerEntry)
class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'account', 'description', 'debit', 'credit')
    list_filter = ('date', 'account')
