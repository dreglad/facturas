# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone

from .models import Comprobante


@shared_task
def validar_comprobante(comp_pk):
    comp = Comprobante.objects.get(comp_pk)
    comp.fecha_validacion = timezone.now()
    comp.save()
