# Generated by Django 4.0.1 on 2022-02-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_team_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='message',
            field=models.CharField(default=False, max_length=1000),
        ),
    ]