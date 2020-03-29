from django.conf import settings
from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=500)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField(blank=True, null=True)
    categoryid = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name