from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Brand(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Car(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    image_url = models.ImageField()


