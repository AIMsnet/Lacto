# Generated by Django 3.0.7 on 2020-06-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lactoApp', '0022_auto_20200618_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='screening_test_date',
            field=models.DateField(blank=True, default=None),
        ),
    ]
