from django.urls import path
from .views import chart_of_accounts, update_chart_of_accounts

app_name = 'accounting'

urlpatterns = [
    path('chart-accounts/', chart_of_accounts, name="chart-accounts"),
    path('chart-accounts/update/<int:pk>', update_chart_of_accounts, name="update-chart-accounts"),
]