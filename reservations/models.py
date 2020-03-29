from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from products.models import Product
from customers.models import Customer

class Timelist(models.Model):
    name = models.CharField(max_length=500)
    visible = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=500)
    visible = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Res(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    customerid = models.ForeignKey(Customer, related_name='order_customer', on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room, related_name='res_room', on_delete=models.CASCADE)
    arrdate = models.DateField(blank=True, null=True)
    starttime = models.ForeignKey(Timelist, related_name='res_starttime', on_delete=models.CASCADE)
    endtime = models.ForeignKey(Timelist, related_name='res_endtime', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.roomid.name} - {self.arrdate}"