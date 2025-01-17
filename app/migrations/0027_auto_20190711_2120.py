# Generated by Django 2.2.2 on 2019-07-11 15:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20190711_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='interested_category',
            field=models.IntegerField(choices=[(1, 'IT/ Telecomunication'), (2, 'Construction/ Engineering/ Architects'), (3, 'Health Care/ Pharma/ Biotech/ Medical/ R&D'), (4, 'Banking/ Insurance/ Financial Services'), (5, 'Teaching/ Education'), (6, 'General Management/ Administration')], null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2019, 7, 26, 21, 20, 42, 124565)),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='jobcategory',
            field=models.IntegerField(choices=[(1, 'IT/ Telecomunication'), (2, 'Construction/ Engineering/ Architects'), (3, 'Health Care/ Pharma/ Biotech/ Medical/ R&D'), (4, 'Banking/ Insurance/ Financial Services'), (5, 'Teaching/ Education'), (6, 'General Management/ Administration')]),
        ),
    ]
