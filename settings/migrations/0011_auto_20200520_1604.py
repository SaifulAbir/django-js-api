# Generated by Django 3.0.3 on 2020-05-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_auto_20200520_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='zoom',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
