
from rest_framework import generics, viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .filters import CarFilter
from .models import Car, Brand
from .permissions import IsAdminOrReadOnly
from .serializers import CarsSerializer, BrandSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CarAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 2

class CarAPIList(generics.ListCreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CarAPIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter


class CarAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CarAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAdminOrReadOnly, )



class BrandAPIList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BrandAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAdminOrReadOnly, )







