# Generated by Django 2.2.2 on 2019-07-08 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190708_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 15, 41, 14, 163733)),
        ),
    ]