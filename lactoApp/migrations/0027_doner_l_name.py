# Generated by Django 3.0.7 on 2020-06-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lactoApp', '0026_auto_20200618_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='doner',
            name='l_name',
            field=models.CharField(blank=True, default=False, max_length=20),
        ),
    ]
