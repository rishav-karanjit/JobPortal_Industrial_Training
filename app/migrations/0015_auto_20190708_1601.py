# Generated by Django 2.2.2 on 2019-07-08 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190708_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 16, 1, 23, 649348)),
        ),
    ]
