# Generated by Django 3.0.3 on 2020-11-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0117_auto_20201108_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='name',
            field=models.IntegerField(max_length=255, primary_key=True, serialize=False),
        ),
    ]