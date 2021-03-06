# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-18 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tcm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testscenarioattributes',
            name='test_scenario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='tcm.TestScenario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testscenariotemplateattributes',
            name='test_scenario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='tcm.TestScenarioTemplate'),
            preserve_default=False,
        ),
    ]
