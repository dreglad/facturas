# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from localflavor.mx.models import MXRFCField



class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notificaciones = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.user)


class Contribuyente(models.Model):
    rfc = MXRFCField(verbose_name='RFC', unique=True)
    cliente = models.ForeignKey('Cliente', related_name='contribuyentes', blank=True)

    def __str__(self):
        return self.rfc

class Comprobante(models.Model):
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    cliente = models.ForeignKey('Cliente', null=True)
    sello = models.CharField(max_length=255, db_index=True)
    total = models.DecimalField(max_digits=9, decimal_places=3)
    emisor_rfc = MXRFCField('RFC del emisor', db_index=True)
    emisor_nombre = models.CharField('nombre del emisor', max_length=255, db_index=True)
    receptor_rfc = MXRFCField('RFC del receptor', db_index=True)
    receptor_nombre = models.CharField('nombre del receptor', max_length=255, db_index=True)
    adjunto_xml = models.ForeignKey('mensajes.Adjunto', related_name="comprobantes_xml", db_index=True, verbose_name='XML Adjunto')
    adjunto_pdf = models.ForeignKey('mensajes.Adjunto', related_name="comprobantes_pdf", null=True, blank=True, verbose_name='PDF Adjunto')
    fecha_validacion = models.DateTimeField('Fecha de validación', blank=True, null=True)

    def __str__(self):
        return 'Comprobante {}'.format(self.pk)