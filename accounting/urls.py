from django.urls import path
from .views import chart_of_accounts, update_chart_of_accounts, home_taxes, update_taxes, delete_taxes

app_name = 'accounting'

urlpatterns = [
    path('chart-accounts/', chart_of_accounts, name="chart-accounts"),
    path('chart-accounts/update/<int:pk>', update_chart_of_accounts, name="update-chart-accounts"),
    path('taxes/', home_taxes, name='taxes'),
    path('taxes/<int:pk>', update_taxes, name='updated-taxes'),
    path('taxes/delete/<int:pk>', delete_taxes, name='delete-taxes'),
]