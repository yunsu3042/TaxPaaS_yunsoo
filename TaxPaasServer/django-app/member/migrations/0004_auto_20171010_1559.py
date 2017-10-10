# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20171010_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxpayerprofile',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile/payer'),
        ),
        migrations.AlterField(
            model_name='taxpractitionerprofile',
            name='clients',
            field=models.ManyToManyField(blank=True, through='member.Connection', to='member.TaxPayerProfile'),
        ),
        migrations.AlterField(
            model_name='taxpractitionerprofile',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile/practitioner'),
        ),
    ]
