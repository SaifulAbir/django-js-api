# Generated by Django 3.0.3 on 2020-09-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0104_auto_20200829_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary_option',
            field=models.CharField(choices=[('AMOUNT', 'Amount'), ('RANGE', 'Range'), ('NEGOTIABLE', 'Negotiable')], default='AMOUNT', max_length=20),
        ),
    ]
