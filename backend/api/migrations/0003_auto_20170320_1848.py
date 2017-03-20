# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170320_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubrole',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='api.Club'),
        ),
    ]
