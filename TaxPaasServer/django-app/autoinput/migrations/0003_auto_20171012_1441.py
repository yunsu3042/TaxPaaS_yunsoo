# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('autoinput', '0002_auto_20171012_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcedoc',
            name='tax_payer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.TaxPayerProfile'),
        ),
        migrations.AddField(
            model_name='w2',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]