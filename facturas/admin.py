# -*- coding: utf-8 -*-
"""Facturas models"""
from django.contrib import admin

from facturas.models import Cliente, Contribuyente, Comprobante


class ContribuyenteInline(admin.TabularInline):
    model = Contribuyente
    extra = 1

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'notificaciones')
    list_filter = ('contribuyentes__rfc',)
    inlines = (ContribuyenteInline,)


@admin.register(Contribuyente)
class ContribuyenteAdmin(admin.ModelAdmin):
    list_display = ('rfc', 'nombre', 'cliente')
    list_filter = ('cliente',)


@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'emisor', 'receptor', 'fecha_timbrado', 'total')
    list_filter = (
        'fecha_timbrado',
        ('emisor', admin.RelatedOnlyFieldListFilter),
        ('receptor', admin.RelatedOnlyFieldListFilter),
    )
    readonly_except = []
    exclude = []
    can_add = False
    can_delete = False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields if f.name not in self.exclude and f.name not in self.readonly_except]

