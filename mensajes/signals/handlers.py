from django.db.models.signals import post_save
from django.dispatch import receiver

from mensajes.models import Adjunto
from mensajes.tasks import buscar_comprobante


@receiver(post_save, sender=Adjunto)
def buscar_comprobante_handler(sender, **kwargs):
    adjunto = kwargs['instance']
    if adjunto.utilizado is None and adjunto.archivo:
        buscar_comprobante.delay(adjunto.pk)
