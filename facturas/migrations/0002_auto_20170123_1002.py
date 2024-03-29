# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 16:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturas', '0001_initial'),
        ('mensajes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='adjunto_pdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comprobantes_pdf', to='mensajes.Adjunto', verbose_name='PDF Adjunto'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='adjunto_xml',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comprobantes_xml', to='mensajes.Adjunto', verbose_name='XML Adjunto'),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturas.Cliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
