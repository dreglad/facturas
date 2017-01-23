from django.db.models.signals import post_save
from django.dispatch import receiver

from facturas.models import Comprobante
from facturas.tasks import validar_comprobante


@receiver(post_save, sender=Comprobante)
def validar_comprobante_handler(sender, **kwargs):
    validar_comprobante.delay(kwargs['instance'].pk)
