# Generated by Django 4.0.1 on 2022-02-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_contact_slug_listing_slug_realtor_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_mvp', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
