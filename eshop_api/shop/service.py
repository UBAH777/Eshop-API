from django_filters import rest_framework as filters
from .models import Item


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ItemFilter(filters.FilterSet):
    year = filters.RangeFilter()
    vendors = CharFilterInFilter(field_name='item__vendor_id', lookup_expr='in')

    class Meta:
        model = Item
        fields = ['year', 'vendor_id']
        