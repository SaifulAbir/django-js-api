# Generated by Django 3.0.3 on 2020-04-09 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0031_job_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.ForeignKey(db_column='company', null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Company'),
        ),
    ]
