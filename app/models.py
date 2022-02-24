from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(blank=True)
    description = models.CharField(max_length=300)
