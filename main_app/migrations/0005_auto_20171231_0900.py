# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_budget_item_expend_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_item',
            name='entry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
