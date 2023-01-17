from django.forms import ModelForm, TextInput, Select, EmailInput
from .models import Industries, Countries, Cities, Customers


class FormIndustry(ModelForm):
    class Meta:
        model = Industries
        fields = '__all__'


class FormCountry(ModelForm):
    class Meta:
        model = Countries
        fields = '__all__'


class FormCities(ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'

customers_field = "form-control"

class FormCustomers(ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={"class":f"{customers_field}"}),
            'last_name': TextInput(attrs={"class":f"{customers_field}"}),
            'job_title': TextInput(attrs={"class":f"{customers_field}"}),
            'gender': Select(attrs={"class":f"{customers_field}"}),
            'phone_number': TextInput(attrs={"class":f"{customers_field}"}),
            'mobil_number': TextInput(attrs={"class":f"{customers_field}"}),
            'email': EmailInput(attrs={"class":f"{customers_field}"}),
            'company_name': TextInput(attrs={"class":f"{customers_field}"}),
            'address': TextInput(attrs={"class":f"{customers_field}"}),
            'postcode': TextInput(attrs={"class":f"{customers_field}"}),
            'tax_id': TextInput(attrs={"class":f"{customers_field}"}),
        }