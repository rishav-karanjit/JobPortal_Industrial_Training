# Generated by Django 2.2.2 on 2019-07-08 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190708_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 15, 46, 7, 257102)),
        ),
    ]