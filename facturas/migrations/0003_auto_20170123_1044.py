# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_auto_20170123_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprobante',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='emisor_nombre',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='emisor_rfc',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='receptor_nombre',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='receptor_rfc',
        ),
        migrations.AddField(
            model_name='comprobante',
            name='emisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comprobantes_emitidos', to='facturas.Contribuyente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='receptor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comprobantes_recibidos', to='facturas.Contribuyente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contribuyente',
            name='nombre',
            field=models.CharField(db_index=True, default='', max_length=255, verbose_name='nombre o razón social'),
            preserve_default=False,
        ),
    ]
