# Generated by Django 3.0.3 on 2020-09-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_auto_20200901_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email_use_tls',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='no_replay_sender_host_password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='no_replay_sender_host_user',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='sender_email_host',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='sender_email_port',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
