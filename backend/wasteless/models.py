import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class ListItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    calories = models.IntegerField()
    purchase_date = models.DateTimeField('Date of purchase')
    expiration_date = models.DateTimeField('Date of expiration')
    consumption_date = models.DateTimeField('Date of consumption')

    def __str__(self):
        return self.name

    def is_expired(self):
        return self.expiration_date <= timezone.now()
