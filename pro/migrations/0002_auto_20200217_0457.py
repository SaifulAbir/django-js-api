# Generated by Django 3.0.3 on 2020-02-17 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200215_0638'),
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='industry_expertise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Industry'),
        ),
    ]
