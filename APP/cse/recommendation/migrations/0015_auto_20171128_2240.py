# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0014_recipe_dish_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pmi',
            name='ingredient1',
        ),
        migrations.RemoveField(
            model_name='pmi',
            name='ingredient2',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='pmi',
            field=models.ManyToManyField(through='recommendation.PMI', to='recommendation.Ingredient'),
        ),
        migrations.AddField(
            model_name='pmi',
            name='ingred1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PMI_ingred1', to='recommendation.Ingredient'),
        ),
        migrations.AddField(
            model_name='pmi',
            name='ingred2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PMI_ingred2', to='recommendation.Ingredient'),
        ),
    ]