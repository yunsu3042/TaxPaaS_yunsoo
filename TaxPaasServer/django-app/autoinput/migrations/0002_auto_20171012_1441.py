# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoinput', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Engine',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]