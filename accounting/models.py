from django.db import models


# Category chart of accounts
class CategoryAccounts(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name


# Chart of Accounts
class ChartOfAccounts(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=220)
    type = models.ForeignKey(CategoryAccounts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} {self.name}'

# Taxes
class Taxes(models.Model):
    code = models.CharField(max_length=10)
    tax_name = models.CharField(max_length=220)
    account_id = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    percentage = models.IntegerField()
