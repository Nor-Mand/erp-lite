from django.shortcuts import render, redirect
from .models import ChartOfAccounts
from .forms import FormChartOfAccounts
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Home Chart of Accounts
@login_required(login_url='login')
def chart_of_accounts(request):
    chartAccounts = ChartOfAccounts.objects.all()
    form = FormChartOfAccounts()
    if request.method == 'POST':
        form = FormChartOfAccounts(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounting:chart-accounts')
    paginator = Paginator(ChartOfAccounts.objects.all(), 10)
    page_number = request.GET.get('page')
    page_accounts = paginator.get_page(page_number)
    context = {
        'chartAccounts': chartAccounts,
        'form': form,
        'page_accounts': page_accounts,
    }
    return render(request, 'chartOfAccounts.html', context)


# Update Chart of Accounts
@login_required(login_url='login')
def update_chart_of_accounts(request, pk):
    chartAccounts = ChartOfAccounts.objects.get(id=pk)
    if request.method == 'POST':
        form = FormChartOfAccounts(request.POST,instance=chartAccounts)
        if form.is_valid():
            form.save()
        return redirect('accounting:chart-accounts')
    else:
        form = FormChartOfAccounts(instance=chartAccounts)
    chartAccounts = ChartOfAccounts.objects.all()
    page_name = request.path
    context = {
        'form': form,
        'page_name': page_name,
        'chartAccounts': chartAccounts,
    }
    return render(request, 'chartOfAccounts.html', context)