# Generated by Django 3.0.3 on 2020-04-15 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0030_auto_20200415_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 15, 5, 9, 35, 564535, tzinfo=utc)),
        ),
    ]
