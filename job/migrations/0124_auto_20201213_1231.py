# Generated by Django 3.0.3 on 2020-12-13 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0123_auto_20201213_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobquestionanswer',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_companies', to='job.Company'),
        ),
    ]
