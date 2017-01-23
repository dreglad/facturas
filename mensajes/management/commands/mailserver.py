#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mail Server"""
import asyncore
import logging
import smtpd

from django.conf import settings
from django.core.management.base import BaseCommand

from mensajes.tasks import correo_recibido

logger = logging.getLogger('main')


class MailServer(smtpd.SMTPServer, object):

    def validate(self, msgdata):
        """Validar mensaje sólo en lo que al mailserver concierne:
           SPAM, abuso, blacklists, TODO: Implementar"""
        return True

    def process_message(self, peer, mailfrom, rcpttos, data):
        """Procesa nuevo mensaje recibido de la calle"""
        if self.validate(data):
            logger.info('Se recibió nuevo correo de: %s', rcpttos)
            correo_recibido.delay(mailfrom, rcpttos, data)
        else:
            logger.warn("Mensaje bloqueado de %s", rcpttos)


class Command(BaseCommand):
    help = 'Inicia servidor de correo SMTP'

    def handle(self, *args, **options):
        logger.debug('Iniciando')
        self.stdout.write(self.style.SUCCESS('Iniciando servidor de correo %s:%s' % (
            settings.MAILSERVER_ADDRESS, settings.MAILSERVER_PORT)))
        MailServer((settings.MAILSERVER_ADDRESS, settings.MAILSERVER_PORT), None)
        try: 
            asyncore.loop()
        except KeyboardInterrupt:
            pass

        
