# Generated by Django 3.0.3 on 2020-10-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0108_jobrecommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrecommendation',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
