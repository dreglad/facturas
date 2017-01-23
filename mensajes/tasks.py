# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from email import message_from_string

from admincfdi.pyutil import ValidCFDI, Global
from celery import shared_task
from django.core.files.base import ContentFile
from lxml import objectify

from facturas.models import Comprobante
from mensajes.models import Adjunto, Mensaje, Destinatario, Remitente


@shared_task
def correo_recibido(mailfrom, rcpttos, data):
    """Nuevo mensaje recibido"""
    mensaje = Mensaje(remitente=Remitente.objects.get_or_create(direccion=mailfrom)[0], contenido=data)
    mensaje.save()

    for addr in rcpttos:
        mensaje.destinatarios.add(Destinatario.objects.get_or_create(direccion=addr)[0])

    mail = message_from_string(data)
    if mail.is_multipart():
        for part in mail.walk():
            if part.get_filename():
                adjunto = Adjunto(tipo=part.get_content_type(), mensaje=mensaje)
                adjunto.archivo.save(part.get_filename(), ContentFile(part.get_payload(decode=True)))
                adjunto.save()
    
    return mensaje.save()


@shared_task
def buscar_comprobante(adjunto_pk):
    """Buscar CFDIs validos en mensaje"""
    adjunto = Adjunto.objects.get(pk=adjunto_pk)
    cfdi = None
    if 'xml' in adjunto.tipo:
        try:
            cfdi = objectify.fromstring(adjunto.archivo.read())
            if not Comprobante.objects.filter(sello=cfdi.attrib['sello']).exists():
                comp = Comprobante(
                    adjunto_xml=adjunto,
                    sello=cfdi.attrib['sello'],
                    total=cfdi.attrib['total'],
                    emisor_rfc=cfdi.Emisor.attrib['rfc'],
                    emisor_nombre=cfdi.Emisor.attrib['nombre'],
                    receptor_rfc=cfdi.Receptor.attrib['rfc'],
                    receptor_nombre=cfdi.Receptor.attrib['nombre'],
                )
                comp.save()
        except Exception as e:
            print(e)
            adjunto.utilizado = False
        else:
            adjunto.utilizado = True
        adjunto.save()
