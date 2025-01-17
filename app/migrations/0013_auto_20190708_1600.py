# Generated by Django 2.2.2 on 2019-07-08 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190708_1556'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='job_category',
            field=models.IntegerField(choices=[(1, 'IT/Telecomunication'), (2, 'Engineering'), (3, 'Medical')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 16, 0, 3, 921241)),
        ),
    ]
