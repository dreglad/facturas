from rest_framework import viewsets, serializers

from facturas.models import Cliente, Comprobante, Contribuyente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 


class ContribuyenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__' 


class ComprobanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comprobante
        fields = '__all__' 


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ContribuyenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer


class ComprobanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Comprobante.objects.all()
    serializer_class = ComprobanteSerializer