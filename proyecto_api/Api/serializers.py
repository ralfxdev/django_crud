from rest_framework import serializers
from Api.models import Cerveza, Botella, Contact

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class CervezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerveza
        fields = '__all__'

class BotellaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Botella
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
