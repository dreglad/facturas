# -*- coding: utf-8 -*-
from django.db import models


class Remitente(models.Model):
    direccion = models.EmailField('dirección', max_length=255, primary_key=True)

    def __str__(self):
        return self.direccion


class Destinatario(models.Model):
    direccion = models.EmailField('dirección', max_length=255, primary_key=True)
    cliente = models.ForeignKey('facturas.Cliente', blank=True)

    def __str__(self):
        return self.direccion


class Adjunto(models.Model):
    archivo = models.FileField(upload_to='adjuntos')
    tipo = models.CharField(max_length=64)
    mensaje = models.ForeignKey('Mensaje', related_name='adjuntos')
    utilizado = models.NullBooleanField(blank=True)

    def __str__(self):
        return '{} ({})'.format(self.archivo.name, self.tipo)


class Mensaje(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    remitente = models.ForeignKey(Remitente)
    destinatarios = models.ManyToManyField(Destinatario, blank=True, related_name='mensajes')
    contenido = models.TextField()

    def __str__(self):
        return 'Mensaje de {} el {}'.format(self.remitente, self.fecha_creacion)
