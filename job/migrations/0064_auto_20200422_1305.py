# Generated by Django 3.0.3 on 2020-04-22 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0063_merge_20200422_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.ForeignKey(db_column='company', default='Unknown', on_delete=django.db.models.deletion.PROTECT, to='job.Company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 7, 3, 9, 75877, tzinfo=utc)),
        ),
    ]
