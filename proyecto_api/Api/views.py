from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from Api import serializers

from rest_framework import viewsets
from Api.models import Cerveza, Botella, Contact
from Api.serializers import CervezaSerializer, BotellaSerializer, ContactSerializer

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

    def destroy(self, request, *args, **kwargs):
        cerveza = self.get_object()
        cerveza.delete()

        return Response({"mensaje": "La cerveza fue eliminada exitosamente."})
    
    def put(self, request, *args, **kwargs):
        cerveza = self.get_object()
        datos_cerveza = request.data

        cerveza.marca = datos_cerveza["marca"]
        cerveza.alcohol = datos_cerveza["alcohol"]
        cerveza.es_artesanal = datos_cerveza["es_artesanal"]
        cerveza.nacionalidad = datos_cerveza["nacionalidad"]

        cerveza.save()

        serializer_class = CervezaSerializer(cerveza)

        return Response(serializer_class.data)

class BotellaViewSet(viewsets.ModelViewSet):
    serializer_class = BotellaSerializer
    queryset = Botella.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def destroy(self, request, *args, **kwargs):
        contact = self.get_object()
        contact.delete()

        return Response({"mensaje": "El contacto fue eliminado exitosamente."})
    
    def put(self, request, *args, **kwargs):
        contact = self.get_object()
        datos_contact = request.data

        contact.name = datos_contact["name"]
        contact.last_name = datos_contact["last_name"]
        contact.email = datos_contact["email"]
        contact.phone = datos_contact["phone"]
        contact.birthday = datos_contact["birthday"]
        contact.social_media = datos_contact["social_media"]

        contact.save()

        serializer_class = ContactSerializer(contact)

        return Response(serializer_class.data)