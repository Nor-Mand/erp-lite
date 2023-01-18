from django.urls import path
from .views import char_of_accounts

app_name = 'accounting'

urlpatterns = [
    path('chart-accounts/', char_of_accounts, name="chart-accounts"),
]