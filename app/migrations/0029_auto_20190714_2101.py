# Generated by Django 2.2.2 on 2019-07-14 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20190711_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 29, 21, 1, 36, 768393)),
        ),
    ]
