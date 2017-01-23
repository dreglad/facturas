"""lafactura URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

from facturas.api import ComprobanteViewSet, ContribuyenteViewSet, ClienteViewSet
from mensajes.api import AdjuntoViewSet, RemitenteViewSet, DestinatarioViewSet, MensajeViewSet

admin.autodiscover()

api_router = routers.DefaultRouter()
api_router.register(r'comprobantes', ComprobanteViewSet)
api_router.register(r'contribuyentes', ContribuyenteViewSet)
api_router.register(r'clientes', ClienteViewSet)
api_router.register(r'adjuntos', AdjuntoViewSet)
api_router.register(r'mensajes', MensajeViewSet)
api_router.register(r'remitentes', RemitenteViewSet)
api_router.register(r'destinatarios', DestinatarioViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns() 

