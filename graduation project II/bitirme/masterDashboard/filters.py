import django_filters

from .models import * 

class MasterFilter(django_filters.FilterSet):
    class Meta:
        model = General
        fields = ['name', 'lectures']