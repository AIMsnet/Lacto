# Generated by Django 3.0.7 on 2020-06-17 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lactoApp', '0005_auto_20200617_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='test1_date',
            field=models.DateField(default=datetime.datetime),
        ),
        migrations.AddField(
            model_name='batch',
            name='test_id',
            field=models.CharField(default=-20, max_length=12),
            preserve_default=False,
        ),
    ]
