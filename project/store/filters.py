from django_filters import rest_framework as filters
from .models import Car

class CarFilter(filters.FilterSet):
    brand = filters.ChoiceFilter(
        field_name='brand',
        choices=lambda: [(brand, brand) for brand in Car.objects.values_list('brand', flat=True).distinct()]
    )

    class Meta:
        model = Car
        fields = ['brand']