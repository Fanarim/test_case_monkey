# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-18 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tcm', '0002_add_scenario_foreignkey_to_attributes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bugs',
            new_name='Bug',
        ),
        migrations.RenameModel(
            old_name='TestScenarioAttributes',
            new_name='TestScenarioAttribute',
        ),
        migrations.RenameModel(
            old_name='TestScenarioTemplateAttributes',
            new_name='TestScenarioTemplateAttribute',
        ),
    ]
