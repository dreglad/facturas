# -*- coding: utf-8 -*-
"""Facturas models"""
from django.contrib import admin

from .models import Adjunto, Destinatario, Mensaje, Remitente



@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'archivo', 'tipo', 'mensaje', 'utilizado')
    can_add = False
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


class AdjuntoInline(admin.TabularInline):
    model = Adjunto
    can_delete = False
    can_add = False
    extra = 0
    readonly_fields = ['archivo', 'tipo', 'utilizado']

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'remitente', '_destinatarios', '_adjuntos')
    inlines = (AdjuntoInline,)
    exclude = ['contenido',]
    editable_fields = tuple()
    can_add = False
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields if f.name not in self.exclude]
    
    def _adjuntos(self, obj):
        return obj.adjuntos.count()

    def _destinatarios(self, obj):
        return ', '.join([dest.direccion for dest in obj.destinatarios.all()])


@admin.register(Remitente)
class RemitenteAdmin(admin.ModelAdmin):
    can_add = False
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]



@admin.register(Destinatario)
class DestinatarioAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'cliente')
