# Generated by Django 3.0.3 on 2020-03-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_merge_20200323_1053'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='skill',
        #     name='job',
        # ),
        migrations.CreateModel(
            name='Job_skill_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(db_column='job', on_delete=django.db.models.deletion.PROTECT, to='job.Job')),
                ('skill', models.ForeignKey(db_column='skill', on_delete=django.db.models.deletion.PROTECT, to='job.Skill')),
            ],
            options={
                'verbose_name': 'Job Skill',
                'verbose_name_plural': 'Job Skills',
                'db_table': 'job_skill_details',
            },
        ),
    ]
