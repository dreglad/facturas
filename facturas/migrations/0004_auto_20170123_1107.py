# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_auto_20170123_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribuyente',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contribuyentes', to='facturas.Cliente'),
        ),
    ]