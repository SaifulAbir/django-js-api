# Generated by Django 3.0.3 on 2020-02-17 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200215_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='contact_email',
            new_name='contact_person_email',
        ),
    ]
