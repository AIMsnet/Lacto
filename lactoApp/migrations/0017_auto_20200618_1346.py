# Generated by Django 3.0.7 on 2020-06-18 08:16

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lactoApp', '0016_batch_collection_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('HBS_test_date', models.DateField(default=datetime.datetime.now)),
                ('HIV_test_date', models.DateField(default=datetime.datetime.now)),
                ('screening_test_date', models.DateField(default=datetime.datetime.now)),
                ('VRDL_test', models.BooleanField()),
                ('VRDL_test_date', models.DateField(default=datetime.datetime.now)),
                ('last_child_birth_date', models.DateField(default=datetime.datetime.now)),
                ('consent', models.BooleanField()),
                ('consent_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='Pasturing_process_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='batch_type',
            field=models.CharField(default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='content1',
            field=models.CharField(default=1, max_length=125),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='doner_id_homo',
            field=models.BooleanField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='exp_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='batch',
            name='pasteurizing_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='batch',
            name='select_type',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='self_other',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='batch',
            name='collection_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
