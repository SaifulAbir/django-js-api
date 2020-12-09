# Generated by Django 3.0.3 on 2020-11-18 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0058_auto_20201104_1715'),
        ('job', '0119_auto_20201109_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('created_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateTimeField(null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateTimeField(null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('question', models.TextField()),
                ('is_anonymous', models.BooleanField(default=False)),
                ('job', models.ForeignKey(db_column='job', on_delete=django.db.models.deletion.PROTECT, related_name='job_question_answers', to='job.Job')),
                ('question_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_questions', to='pro.Professional')),
            ],
            options={
                'verbose_name': 'Job Question Answer',
                'verbose_name_plural': 'Job Question Answers',
                'db_table': 'job_question_answers',
            },
        ),
    ]