# Generated by Django 3.0.3 on 2020-07-11 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0047_auto_20200704_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
