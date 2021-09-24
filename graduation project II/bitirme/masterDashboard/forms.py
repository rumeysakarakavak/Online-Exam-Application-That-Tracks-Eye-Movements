from django.forms import ModelForm
from .models import General


class GeneralForm(ModelForm):
    class Meta:
        model = General
        fields = '__all__'