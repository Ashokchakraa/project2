from django.db import models

from django.db.models.signals import pre_save

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    costPerItem = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField()
    volume = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


def calcucate_volume(instance, sender, *args, **kwargs):
    instance.volume = float(instance.costPerItem * instance.stockQuantity)


pre_save.connect(calcucate_volume, sender=Product)