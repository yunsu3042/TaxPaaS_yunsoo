# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-21 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxorg', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('age', models.DateField(null=True)),
                ('user_type', models.CharField(blank=True, choices=[('PY', 'tax_payer'), ('PT', 'tax_practitioner'), ('SU', 'super_user')], max_length=20, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('registration_id', models.CharField(max_length=300, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('task', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TaxPayerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile/payer')),
                ('organizer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxorg.TaxOrganizer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaxPractitionerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_certificated', models.BooleanField(default=False)),
                ('locals', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile/practitioner')),
                ('clients', models.ManyToManyField(blank=True, through='member.Connection', to='member.TaxPayerProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='tax_payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.TaxPayerProfile'),
        ),
        migrations.AddField(
            model_name='connection',
            name='tax_practitioner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.TaxPractitionerProfile'),
        ),
    ]
