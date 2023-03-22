from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from item.models import Item

User = get_user_model()


class Order(models.Model):
    customer_text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    buyer = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='orders')
    items = models.ManyToManyField(to=Item, related_name='orders', through='OrderedItems')

    def __str__(self):
        return f'{self.id} - Order ref {self.customer_text}'


class OrderedItems(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.PROTECT)
    item = models.ForeignKey(to=Item, on_delete=models.PROTECT)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
