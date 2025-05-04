from django.shortcuts import render, redirect
from .models import LedgerEntry
from .forms import LedgerEntryForm

def ledger_index(request):
    entries = LedgerEntry.objects.select_related('account').order_by('-date')
    if request.method == 'POST':
        form = LedgerEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger-index')
    else:
        form = LedgerEntryForm()
    return render(request, 'accounts/index.html', {'entries': entries, 'form': form})
