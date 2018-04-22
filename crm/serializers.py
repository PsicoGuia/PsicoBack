from rest_framework import serializers
from .models import Person



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('company_name',)
