from django.forms import ModelForm
from django.forms.widgets import TextInput, DateTimeInput, NumberInput, CheckboxInput
from .models import ChartOfAccounts, Taxes, Currency


class FormChartOfAccounts(ModelForm):
    class Meta:
        model = ChartOfAccounts
        fields = '__all__'


class FormTaxes(ModelForm):
    class Meta:
        model = Taxes
        fields = '__all__'


class FormCurrency(ModelForm):

    class Meta:
        currency_field = "form-control"
        model = Currency
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={"class": f"{currency_field}"}),
            'abbrev': TextInput(attrs={"class": f"{currency_field}"}),
            'symbol': TextInput(attrs={"class": f"{currency_field}"}),
            'date': DateTimeInput(attrs={'type': 'date', "class": f"{currency_field}"}),
            'rate': NumberInput(attrs={"class": f"{currency_field}"}),
            'status': CheckboxInput(attrs={"type": "checkbox",
                                         "class": "form-check-input"}),
        }