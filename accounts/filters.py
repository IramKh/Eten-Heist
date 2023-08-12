import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Our_Product
        fields = '__all__'
        