# Generated by Django 3.0.3 on 2020-03-02 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='currency',
            field=models.ForeignKey(blank=True, db_column='currency', null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Currency'),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
