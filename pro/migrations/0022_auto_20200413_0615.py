# Generated by Django 3.0.3 on 2020-04-13 06:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import p7.validators


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0029_merge_20200405_1001'),
        ('pro', '0021_merge_20200330_0338'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'certificate_names',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'institutes',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'majors',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'nationalities',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.AddField(
            model_name='professional',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='professional',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='professional',
            name='expected_salary_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='expected_salary_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Experience'),
        ),
        migrations.AddField(
            model_name='professional',
            name='facebbok_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='father_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Gender'),
        ),
        migrations.AddField(
            model_name='professional',
            name='linkedin_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='mother_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='qualification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Qualification'),
        ),
        migrations.AddField(
            model_name='professional',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.JobType'),
        ),
        migrations.AddField(
            model_name='professional',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('Started_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.Company')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'work_experiences',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current_position', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, validators=[p7.validators.check_valid_phone_number])),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'references',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('verified_by_skillcheck', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.Skill')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'professional_skills',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgpa', models.CharField(blank=True, max_length=255, null=True)),
                ('enrolled_date', models.DateField(blank=True, null=True)),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pro.Institute')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pro.Major')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='job.Qualification')),
            ],
            options={
                'db_table': 'professional_educations',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'portfolios',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_held', models.CharField(blank=True, max_length=255, null=True)),
                ('membership_ongoing', models.BooleanField(default=False)),
                ('Start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('desceription', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('org_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Organization')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'memberships',
            },
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_expiry_period', models.BooleanField(default=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('credential_id', models.CharField(blank=True, max_length=255, null=True)),
                ('credential_url', models.CharField(blank=True, max_length=255, null=True)),
                ('certification_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.CertificateName')),
                ('organization_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Organization')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pro.Professional')),
            ],
            options={
                'db_table': 'certifications',
            },
        ),
        migrations.AddField(
            model_name='professional',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pro.Nationality'),
        ),
    ]
