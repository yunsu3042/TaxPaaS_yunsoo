# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20171010_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxpractitionerprofile',
            name='clients',
            field=models.ManyToManyField(blank=True, through='member.Connection', to='member.TaxPayerProfile'),
        ),
    ]
