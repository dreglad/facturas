# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from email import message_from_string
import logging

from admincfdi.pyutil import ValidCFDI, Global
from celery import shared_task
from django.core.files.base import ContentFile
from lxml import objectify

from facturas.models import Comprobante, Contribuyente
from mensajes.models import Adjunto, Mensaje, Destinatario, Remitente

logger = logging.getLogger('main')

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
    logger.info("Buscando comprobante en nuevo Adjunto")
    adjunto = Adjunto.objects.get(pk=adjunto_pk)
    if 'xml' in adjunto.tipo:
        try:
            cfdi = objectify.fromstring(adjunto.archivo.read())

            receptor, nuevo = Contribuyente.objects.get_or_create(rfc=cfdi.Receptor.attrib['rfc'])
            if nuevo:
                receptor.nombre = cfdi.Receptor.attrib['nombre']
                receptor.save()
                logger.debug("Receptor no registrado, se registró nuevo Contribuyente: %s", emisor)

            emisor, nuevo = Contribuyente.objects.get_or_create(rfc=cfdi.Emisor.attrib['rfc'])
            if nuevo:
                emisor.nombre = cfdi.Emisor.attrib['nombre']
                emisor.save()
                logger.debug("Emisor no registrado, se registró nuevo Contribuyente: %s", emisor)

            if not Comprobante.objects.filter(sello=cfdi.attrib['sello']).exists():
                comp = Comprobante(
                    emisor=emisor, receptor=receptor, adjunto_xml=adjunto,
                    sello=cfdi.attrib['sello'], total=cfdi.attrib['total']
                    )
                comp.save()
            else:
                logger.info('Comprobante duplicado, no se añadió: %s', comp)
        except Exception as e:
            logger.warn(e)
            adjunto.utilizado = False
            logger.info("Adjunto no utilizado: %s", adjunto)
        else:
            adjunto.utilizado = True
            logger.info("Adjunto utilizado, comporbante creado: %s", comp)

        adjunto.save()
