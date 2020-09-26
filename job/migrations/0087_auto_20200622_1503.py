# Generated by Django 3.0.3 on 2020-06-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0086_auto_20200622_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True),
        ),
    ]
