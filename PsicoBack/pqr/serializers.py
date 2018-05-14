from rest_framework import serializers
from .models import requestPQR


class requestPQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestPQR
        fields = '__all__'


class requestPQRDetailSerializer(requestPQRSerializer):
    class Meta:
        model = requestPQR
        fields = '__all__'
