from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from Api import serializers

from rest_framework import viewsets
from Api.models import Cerveza, Botella
from Api.serializers import CervezaSerializer, BotellaSerializer

# Create your views here.

class HelloAPIView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Hello Wordl"
        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    serializers_class = serializers.HelloSerializer

    #Creamos el método POST

    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})
    
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})


class CervezaViewSet(viewsets.ModelViewSet):
    serializer_class = CervezaSerializer
    queryset = Cerveza.objects.all()

class BotellaViewSet(viewsets.ModelViewSet):
    serializer_class = BotellaSerializer
    queryset = Botella.objects.all()

# class PersonViewSet(viewsets.ModelViewSet):
#     serializers_class = PersonSerializer
#     queryset = Person.objects.all()