# Generated by Django 3.0.3 on 2020-05-04 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0071_auto_20200503_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='approve_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_category',
            field=models.ForeignKey(blank=True, db_column='job_category', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='job.JobCategory'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_gender',
            field=models.ForeignKey(blank=True, db_column='job_gender', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='job.JobGender'),
        ),
        migrations.AlterField(
            model_name='job',
            name='post_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
