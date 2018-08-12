from rest_framework import serializers
from .models import requestPQR, FAQ


class requestPQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestPQR
        fields = '__all__'


class requestPQRDetailSerializer(requestPQRSerializer):
    class Meta:
        model = requestPQR
        fields = '__all__'


class FAQSerializer(requestPQRSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
