# Generated by Django 3.0.3 on 2020-08-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0099_auto_20200809_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='locked_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
