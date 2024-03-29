# Generated by Django 3.0.3 on 2020-05-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0076_auto_20200521_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='other_benefits',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trendingkeywords',
            name='keyword',
            field=models.CharField(max_length=255),
        ),
    ]
