from django.db import models
from datetime import datetime


class Project(models.Model):
    slug = models.CharField(max_length=200, unique=True, null=False)
    title = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    has_shop = models.BooleanField(default=False)
    has_apartments = models.BooleanField(default=False)
    has_office = models.BooleanField(default=False)
    has_houses = models.BooleanField(default=False)
    has_plots = models.BooleanField(default=False)
    has_penthouses = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
