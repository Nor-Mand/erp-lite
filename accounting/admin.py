from django.contrib import admin
from .models import CategoryAccounts, Currency, ChartOfAccounts


admin.site.register(CategoryAccounts)
admin.site.register(Currency)
admin.site.register(ChartOfAccounts)

