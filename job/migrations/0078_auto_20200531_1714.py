# Generated by Django 3.0.3 on 2020-05-31 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0077_auto_20200531_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company_name',
            new_name='company',
        ),
    ]
