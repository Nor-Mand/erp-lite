from django.shortcuts import render, redirect
from .models import ChartOfAccounts, Taxes, Currency
from .forms import FormChartOfAccounts, FormTaxes, FormCurrency
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


# Taxes
@login_required(login_url='login')
def home_taxes(request):
    form = FormTaxes()
    if request.method == 'POST':
        form = FormTaxes(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounting:taxes')
    taxes = Taxes.objects.all()
    paginator = Paginator(Taxes.objects.all(), 6)
    page_number = request.GET.get('page')
    page_taxes = paginator.get_page(page_number)
    context = {
        'form': form,
        'taxes': form,
        'page_taxes': page_taxes,
    }
    return render(request,'taxes.html', context)


# Taxes Update
@login_required(login_url='page')
def update_taxes(request, pk):
    taxes = Taxes.objects.get(id=pk)
    if request.method == 'POST':
        form = FormTaxes(request.POST, instance=taxes)
        if form.is_valid():
            form.save()
        return redirect('accounting:taxes')
    else:
        form = FormTaxes(instance=taxes)
    page_taxes = Taxes.objects.all()
    page_name = request.path
    context = {
        'form': form,
        'page_taxes': page_taxes,
        'page_name': page_name
    }
    return render(request, 'taxes.html', context)


# Tax Delete
@login_required(login_url='page')
def delete_taxes(request, pk):
    taxes = Taxes.objects.get(id=pk)
    taxes.delete()
    return redirect(request, 'taxes.html')


# Currency
@login_required(login_url='page')
def home_currency(request):
    form = FormCurrency()
    if request.method == 'POST':
        form = FormCurrency(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounting:currency')
    currencies = Currency.objects.all()
    context = {
        'form': form,
        'currencies': currencies,
    }
    return render(request, 'currency.html', context)


# Update Currency
@login_required(login_url='login')
def update_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    if request.method == 'POST':
        form = FormCurrency(request.POST, instance=currency)
        if form.is_valid():
            form.save()
        return redirect('accounting:currency')
    else:
        form = FormCurrency(instance=currency)
    context = {
        'form': form,
    }
    return render(request, 'currency.html', context)