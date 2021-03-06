from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializer


class HelloAPIView(APIView):
    """API View de Prueba"""

    serializer_class = serializer.HelloSerializer


    def get(self, request, format=None):
        """Retornar lista de caracteristicas del APIView"""
        an_apiview = [
            'Usamos Metodos HTTP como funciones (get , post, put, patch, delete) ',
            'Es similar a una vista tradicional de django',
            'Nos da el mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Maneja actualizar un objeto"""
        return Response({'method' : 'PUT'})

    def patch(self,request, pk=None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method' : 'PATCH'})

    def delete(self,request, pk=None):
        """Maneja Borrar un objeto"""
        return Response({'method' : 'DELETE'})