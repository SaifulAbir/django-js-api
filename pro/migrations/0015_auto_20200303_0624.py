# Generated by Django 3.0.3 on 2020-03-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0014_auto_20200303_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
