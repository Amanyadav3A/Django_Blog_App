# Generated by Django 5.1.4 on 2025-01-22 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_input_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input_post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 15, 2, 10, 303441)),
        ),
    ]
