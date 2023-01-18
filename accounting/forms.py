from django.forms import ModelForm
from .models import ChartOfAccounts


class FormChartOfAccounts(ModelForm):
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'