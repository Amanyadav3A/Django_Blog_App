# Generated by Django 5.1.4 on 2025-01-08 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 8, 7, 34, 43, 459045)),
        ),
    ]
