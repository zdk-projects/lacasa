# Generated by Django 4.0.1 on 2022-02-01 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0007_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='message',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]