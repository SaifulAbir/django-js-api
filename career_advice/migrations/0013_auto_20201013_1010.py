# Generated by Django 3.0.3 on 2020-10-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_advice', '0012_careeradvice_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careeradvice',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]