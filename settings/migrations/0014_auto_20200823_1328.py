# Generated by Django 3.0.3 on 2020-08-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_auto_20200625_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='address',
            field=models.TextField(),
        ),
    ]
