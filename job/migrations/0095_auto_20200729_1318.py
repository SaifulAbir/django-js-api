# Generated by Django 3.0.3 on 2020-07-29 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0094_auto_20200729_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationstatus',
            old_name='status',
            new_name='name',
        ),
    ]
