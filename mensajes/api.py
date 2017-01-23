from rest_framework import viewsets, serializers

from mensajes.models import Adjunto, Mensaje, Remitente, Destinatario


class AdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjunto
        fields = '__all__' 


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__' 


class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = '__all__' 


class RemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remitente
        fields = '__all__' 



class AdjuntoViewSet(viewsets.ModelViewSet):
    queryset = Adjunto.objects.all()
    serializer_class = AdjuntoSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class RemitenteViewSet(viewsets.ModelViewSet):
    queryset = Remitente.objects.all()
    serializer_class = RemitenteSerializer


class DestinatarioViewSet(viewsets.ModelViewSet):
    queryset = Destinatario.objects.all()
    serializer_class = DestinatarioSerializer

