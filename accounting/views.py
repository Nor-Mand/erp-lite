from django.shortcuts import render, redirect, HttpResponse
from .models import ChartOfAccounts, Taxes, Currency, CategoryAccounts
from .forms import FormChartOfAccounts, FormTaxes, FormCurrency
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import csv
import os

# Home Chart of Accounts
@login_required(login_url='login')
def chart_of_accounts(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    account_filter = ChartOfAccounts.objects.filter(
        Q(name__icontains=q)
    )
    chartAccounts = ChartOfAccounts.objects.all()
    form = FormChartOfAccounts()
    if request.method == 'POST':
        form = FormChartOfAccounts(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounting:chart-accounts')
    # paginator = Paginator(ChartOfAccounts.objects.all(), 15)
    paginator = Paginator(account_filter, 15)
    page_number = request.GET.get('page')
    page_accounts = paginator.get_page(page_number)
    context = {
        'chartAccounts': chartAccounts,
        'form': form,
        'page_accounts': page_accounts,
        # 'account_filter': account_filter
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

# Delete Char of Accounts
@login_required(login_url='login')
def delete_chart_of_accounts(request, pk):
    chartAccounts = ChartOfAccounts.objects.get(id=pk)
    chartAccounts.delete()
    return redirect('accounting:chart-accounts')

# Char of Account Import CSV
@login_required(login_url='login')
def import_chart_of_account(request):
    accounts = []
    with open("accounts.csv", "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data[1:]:
            accounts.append(
                ChartOfAccounts(
                    code=row[0],
                    name=row[1],
                    type=CategoryAccounts.objects.get(name=row[2])
                )
            )
    if len(accounts) > 0:
        ChartOfAccounts.objects.bulk_create(accounts)
    return HttpResponse("Succesfully Imported")


# Chart of Account Export CSV
@login_required(login_url='login')
def char_of_account_export(request):
    response = HttpResponse(content_type='type/csv')
    response['Content-Disposition'] = 'attachment; filename=accounts.csv'
    writer = csv.writer(response)
    accounts = ChartOfAccounts.objects.all()
    writer.writerow(['Code', 'Name', 'Type'])

    for account in accounts:
        writer.writerow(([account.code, account.name, account.type]))
    return response


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
    obj = Currency.objects.get(id=pk)
    if request.method == 'POST':
        form = FormCurrency(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        return redirect('accounting:currency')
    else:
        form = FormCurrency(instance=obj)
    context = {
        'form': form,
        'obj': obj
    }
    return render(request, 'updateCurrency.html', context)

# Delete Currencey
@login_required(login_url='login')
def delete_currency(request, pk):
    currency = Currency.objects.get(id=pk)
    currency.delete()
    return redirect('accounting:currency')

# Bank account
def bank_account(request):
    return render(request, 'bankAccount.html')