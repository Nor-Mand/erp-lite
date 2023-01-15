from django.forms import ModelForm
from .models import Industries, Countries, Cities


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