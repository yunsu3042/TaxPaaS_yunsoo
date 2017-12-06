# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autoinput', '0008_auto_20171129_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ten99div',
            name='name',
        ),
        migrations.AddField(
            model_name='ten99div',
            name='account_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='cash_liquidation_distributions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='city_check',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='collectibles_gain',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='cut_end_points',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='cut_start_points',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='exempt_interest_dividends',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='fatca_filling',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='federal_income_tax',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='foreign_country_possession',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='foreign_tax',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='ten99int'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ten99div',
            name='investment_expense',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='noncash_liquidation_distributions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='nondividend_distributions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='payer_federal_in',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='payer_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='recipient_first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='recipient_in',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='recipient_last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='section_1202_gain',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='specified_private_activity_bond',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='state_check',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='state_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='state_recheck',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='state_tax',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='street_address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='street_address_recheck',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='total_capital_gain_distr',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='total_ordinary_dividends',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='unrecap',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='zip_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='ten99div',
            name='zip_code_check',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='ten99div',
            name='qualified_dividends',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
