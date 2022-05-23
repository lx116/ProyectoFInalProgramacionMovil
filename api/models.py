from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    image = models.ImageField(null=True)
    
    def __str(self):
        return self.name


class Stock(models.Model):
    available_quantity = models.IntegerField(null=True)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    date = models.DateField(null=True)
    total = models.FloatField(null=True)
    sub_total = models.FloatField(null=True)
    user = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.date.strftime('FECHA: %d/%m/%y  HORA: %H:%M:%S')


class ItemOrder(models.Model):
    name = models.CharField(null=True, default='a', max_length=100)
    quantity = models.IntegerField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    total_value = models.FloatField(null=True, default=0)
    total_cost = models.FloatField(null=True, default=0)
    individual_value = models.FloatField(null=True, default=0)
    individual_cost = models.FloatField(null=True, default=0)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        self.name = self.product.name
        return self.product.name


class Pay(models.Model):
    pass


class Record(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    creation_date = models.DateField(null=True)
    user = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


