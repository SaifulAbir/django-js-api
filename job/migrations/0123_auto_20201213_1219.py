# Generated by Django 3.0.3 on 2020-12-13 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0058_auto_20201104_1715'),
        ('job', '0122_jobquestionanswer_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobquestionanswer',
            name='question_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_questions', to='pro.Professional'),
        ),
    ]
