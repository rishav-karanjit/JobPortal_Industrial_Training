# Generated by Django 2.2.2 on 2019-07-08 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190708_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 15, 32, 19, 470438)),
        ),
    ]
