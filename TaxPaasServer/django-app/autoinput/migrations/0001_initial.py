# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DividendIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SourceDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('M', 'Mine'), ('S', 'Spouse'), ('D', 'Dependents')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('job_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ten95B',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
        migrations.CreateModel(
            name='Ten95C',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=30)),
                ('ssn', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
        migrations.CreateModel(
            name='Ten98',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mortgage_interest', models.CharField(blank=True, max_length=30)),
                ('refund', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
        migrations.CreateModel(
            name='Ten99DIV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualified_dividends', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
        migrations.CreateModel(
            name='Ten99INT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.CharField(blank=True, max_length=30)),
                ('interest_income', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
        migrations.CreateModel(
            name='W2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='w2')),
                ('auto_start', models.BooleanField(default=False)),
                ('ssn', models.CharField(blank=True, max_length=50)),
                ('ein', models.CharField(blank=True, max_length=50)),
                ('wage', models.CharField(blank=True, max_length=20)),
                ('federal_income', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('ss_wages', models.CharField(blank=True, max_length=30)),
                ('ss_tax', models.CharField(blank=True, max_length=30)),
                ('medicare_wages', models.CharField(blank=True, max_length=30)),
                ('medicare_tax', models.CharField(blank=True, max_length=30)),
                ('ss_tips', models.CharField(blank=True, max_length=30)),
                ('all_tips', models.CharField(blank=True, max_length=30)),
                ('control_number', models.CharField(blank=True, max_length=30)),
                ('dp_care_benefits', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('zip_code', models.CharField(blank=True, max_length=30)),
                ('nq_plans', models.CharField(blank=True, max_length=30)),
                ('box12a', models.CharField(blank=True, max_length=30)),
                ('box12b', models.CharField(blank=True, max_length=30)),
                ('box12c', models.CharField(blank=True, max_length=30)),
                ('box12d', models.CharField(blank=True, max_length=30)),
                ('st_employee', models.CharField(blank=True, max_length=30)),
                ('retire_plan', models.CharField(blank=True, max_length=30)),
                ('tp_sick_pay', models.CharField(blank=True, max_length=30)),
                ('other', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('st_id_number', models.CharField(blank=True, max_length=30)),
                ('st_wages', models.CharField(blank=True, max_length=30)),
                ('st_tax', models.CharField(blank=True, max_length=30)),
                ('locality_name', models.CharField(blank=True, max_length=30)),
                ('lc_wages', models.CharField(blank=True, max_length=30)),
                ('lc_tax', models.CharField(blank=True, max_length=30)),
                ('source_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoinput.SourceDoc')),
            ],
        ),
    ]
