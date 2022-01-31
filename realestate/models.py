from django.core.exceptions import ValidationError
from django.db import models


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
