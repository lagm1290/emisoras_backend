from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from .models import Emisora
from .serializers import EmisoraSerializer


class EmisoraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Emisora.objects.all()
    serializer_class = EmisoraSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'cadena', 'ciudad']

    def get_queryset(self):
        queryset = Emisora.objects.all()
        cadena = self.request.query_params.get('cadena')
        ciudad = self.request.query_params.get('ciudad')

        if cadena:
            queryset = queryset.filter(cadena=cadena)
        if ciudad:
            queryset = queryset.filter(ciudad=ciudad)

        return queryset


@api_view(['GET'])
def cadenas_list(request):
    cadenas = (
        Emisora.objects.values('cadena')
        .annotate(count=Count('id'))
        .order_by('cadena')
    )
    return Response(list(cadenas))


@api_view(['GET'])
def ciudades_list(request):
    ciudades = (
        Emisora.objects.values('ciudad')
        .annotate(count=Count('id'))
        .order_by('ciudad')
    )
    return Response(list(ciudades))
