from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.name}'


@receiver(pre_delete, sender=Item)
def protect_item(sender, instance, **kwargs):
    if instance.orders.exists():
        raise ValidationError("Can't delete this item. It is related to one or more orders!")
