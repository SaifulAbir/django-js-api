# Generated by Django 3.0.3 on 2020-04-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0030_auto_20200411_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True),
        ),
    ]
