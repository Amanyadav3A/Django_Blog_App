# Generated by Django 5.1.4 on 2025-01-23 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_input_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_post',
            name='user_comment',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='input_post',
            name='user_like',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='input_post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 23, 14, 23, 28, 394155)),
        ),
    ]
