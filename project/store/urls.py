from django.urls import path
from .views import *
urlpatterns = [
    path('api/v1/cars/', CarAPIList.as_view()),
    path('api/v1/car/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/car_delete/<int:pk>/', CarAPIDestroy.as_view()),
    path('api/v1/brands/', BrandAPIList.as_view()),
    path('api/v1/brand/<int:pk>/', BrandAPIUpdate.as_view()),

]
