from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Person


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(required=False, read_only=True, many=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "groups"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonDetailSerializer(PersonSerializer):
    user = UserSerializer(required=False, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'
