# Generated by Django 3.0.7 on 2020-06-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lactoApp', '0025_auto_20200618_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='f_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
