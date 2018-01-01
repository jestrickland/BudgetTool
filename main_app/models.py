from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Budget_Item(models.Model):

    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=100)
    expend_category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_month = models.IntegerField(default=1)
    entry_day = models.IntegerField(default=1)
    entry_year = models.IntegerField(default=1)
    #entry_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
