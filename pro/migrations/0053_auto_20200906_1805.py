# Generated by Django 3.0.3 on 2020-09-06 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0052_auto_20200809_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='professional',
            options={'ordering': ['-created_at'], 'verbose_name': 'Professional', 'verbose_name_plural': 'Professionals'},
        ),
    ]
