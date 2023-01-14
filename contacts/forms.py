from django.forms import ModelForm
from .models import Industries


class FormIndustry(ModelForm):
    class Meta:
        model = Industries
        fields = '__all__'