# Generated by Django 3.0.3 on 2020-06-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0083_auto_20200609_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='documents'),
        ),
    ]
