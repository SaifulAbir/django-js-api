# Generated by Django 3.0.3 on 2020-02-16 09:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('professional_id', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('industry_expertise', models.CharField(blank=True, max_length=255, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Professional',
                'verbose_name_plural': 'Professionals',
                'db_table': 'professionals',
            },
        ),
    ]
