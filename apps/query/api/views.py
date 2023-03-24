from rest_framework import viewsets

from ..models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API que retorna todos informacion de todos los clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filterset_fields = ['cc', 'nit','pasaporte']


