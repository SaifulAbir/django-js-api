# Generated by Django 3.0.3 on 2020-09-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_auto_20200913_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='admin_email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='support_email',
            field=models.CharField(max_length=50),
        ),
    ]
