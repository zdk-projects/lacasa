from django.core.exceptions import ValidationError
from django.db import models

from django.db import models
from datetime import datetime


# Create your models here.
class AboutUs(models.Model):
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    show_phone_number = models.BooleanField(default=False, )

    second_phone_number = models.CharField(max_length=14, null=True, blank=True)
    show_second_phone_number = models.BooleanField(default=False, )

    office_phone_number = models.CharField(max_length=14, null=True, blank=True)
    show_office_phone_number = models.BooleanField(default=False, )

    office_address = models.CharField(max_length=256, null=True, blank=True)
    show_office_address = models.BooleanField(default=False, )

    # SOCIAL MEDIA LINKS

    email_address = models.CharField(max_length=100, null=True, blank=True)
    show_email_address = models.BooleanField(default=False, )

    facebook_link = models.CharField(max_length=256, null=True, blank=True)
    show_facebook_link = models.BooleanField(default=False, )

    twitter_link = models.CharField(max_length=256, null=True, blank=True)
    show_twitter_link = models.BooleanField(default=False, )

    youtube_link = models.CharField(max_length=256, null=True, blank=True)
    show_youtube_link = models.BooleanField(default=False, )

    linked_link = models.CharField(max_length=256, null=True, blank=True)
    show_linked_link = models.BooleanField(default=False, )

    instagram_link = models.CharField(max_length=256, null=True, blank=True)
    show_instagram_link = models.BooleanField(default=False, )

    class Meta:
        db_table = "tbl_about_us"
        verbose_name = 'About Us List'

    def __str__(self):
        return f"{self.phone_number}"

    def save(self, *args, **kwargs):
        # count will have all of the objects from the Aboutus model
        count = AboutUs.objects.all().count()
        # this will check if the variable exist so we can update the existing ones
        save_permission = AboutUs.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count < 1:
            super(AboutUs, self).save()
        elif save_permission:
            super(AboutUs, self).save()

    def has_add_permission(self):
        return AboutUs.objects.filter(id=self.id).exists()


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, null=False)

    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, null=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class HomeListing(models.Model):
    realtor = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, null=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    message = models.CharField(max_length=1000, default=False)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_mvp = models.BooleanField(default=False)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    achievement_description = models.CharField(max_length=2000, null=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
