# Generated by Django 3.0.3 on 2020-12-13 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0121_auto_20201213_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobquestionanswer',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='job_companies', to='job.Company'),
            preserve_default=False,
        ),
    ]
