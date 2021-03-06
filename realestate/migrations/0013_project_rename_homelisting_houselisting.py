# Generated by Django 4.0.1 on 2022-02-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0012_homelisting_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('tag_line', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('has_shop', models.BooleanField(default=False)),
                ('has_apartments', models.BooleanField(default=False)),
                ('has_office', models.BooleanField(default=False)),
                ('has_houses', models.BooleanField(default=False)),
                ('has_plots', models.BooleanField(default=False)),
                ('has_penthouses', models.BooleanField(default=False)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.RenameModel(
            old_name='HomeListing',
            new_name='HouseListing',
        ),
    ]
