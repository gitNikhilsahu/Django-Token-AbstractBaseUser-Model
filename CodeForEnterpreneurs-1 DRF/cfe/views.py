from rest_framework.response import Response
from rest_framework import viewsets

from cfe import serializers


class cfe_view_set(viewsets.ViewSet):
    serializer_class = serializers.CFESerializer

    def list(self, request):
        a_viewset = [
            'cfe home list view'
        ]

        return Response({'message': 'CFE!', 'a_viewset': a_viewset})
