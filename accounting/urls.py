from django.urls import path
from .views import *

app_name = 'accounting'

urlpatterns = [
    path('chart-accounts/', chart_of_accounts, name="chart-accounts"),
    path('chart-accounts/update/<int:pk>', update_chart_of_accounts, name="update-chart-accounts"),
    path('chart-accounts/delete/<int:pk>', delete_chart_of_accounts, name="delete-chart-accounts"),
    path('chart-accounts/csv_export/', char_of_account_export, name='export-accounts'),
    path('chart-accounts/csv_import/', import_chart_of_account, name='import-accounts'),
    path('taxes/', home_taxes, name='taxes'),
    path('taxes/<int:pk>', update_taxes, name='updated-taxes'),
    path('taxes/delete/<int:pk>', delete_taxes, name='delete-taxes'),
    path('currency/', home_currency, name='currency'),
    path('currency/<int:pk>', update_currency, name='update-currency'),
    path('currency/delete/<int:pk>', delete_currency, name='delete-currency'),
    path('bank-account/', bank_account, name="bank-account"),
]