from django.forms import ModelForm
from .models import ChartOfAccounts, Taxes


class FormChartOfAccounts(ModelForm):
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'


class FormTaxes(ModelForm):
    class Meta:
        model = Taxes
        fields = '__all__'