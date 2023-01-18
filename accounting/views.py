from django.shortcuts import render
from .models import ChartOfAccounts


# Home Chart of Accounts
def char_of_accounts(request):
    return render(request, 'chartOfAccounts.html')
