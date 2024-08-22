from django.db import models


class Order(models.Model):
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Discount(models.Model):
    code = models.IntegerField()
    active = models.BooleanField(default=True)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)


