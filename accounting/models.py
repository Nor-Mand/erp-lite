from django.db import models


# Category chart of accounts
class CategoryAccounts(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name


# Chart of Accounts
class ChartOfAccounts(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=220)
    type = models.ForeignKey(CategoryAccounts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} {self.name}'

    class Meta:
        ordering = ['code']


# Taxes
class Taxes(models.Model):
    code = models.CharField(max_length=10)
    tax_name = models.CharField(max_length=220)
    account_id = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    percentage = models.IntegerField()


# Currency
class Currency(models.Model):
    name = models.CharField(max_length=220)
    symbol = models.CharField(max_length=5)
    abbrev = models.CharField(max_length=10)
    date = models.DateField()
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField()


# Journal Entryes
class JournalEntries(models.Model):
    date = models.DateField()
    account_id = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    reference = models.CharField(max_length=250)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)