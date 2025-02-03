# Generated by Django 5.1.4 on 2025-01-22 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_input_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_post',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='input_post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 13, 49, 21, 176197)),
        ),
    ]
