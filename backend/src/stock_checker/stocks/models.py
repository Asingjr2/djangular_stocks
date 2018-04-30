from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxLengthValidator
from django.urls import reverse

from base.models import BaseModel

class Stock(BaseModel):
    ticker = models.CharField(max_length= 4)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return "{} stock ticker".format(self.ticker)

    def get_absolute_url(self):
        return reverse('stock_detail', args=(self.id,))

class Favorites(BaseModel):
    stock = models.ManyToManyField(Stock)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
