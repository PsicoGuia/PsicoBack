from rest_framework import serializers
from .models import Profile, Studies, Office, Chat,\
    CategoryPatology, Patology, ProfilePatologyOrCategory,\
    RequestOrderMedicDate, ScheduleAttentionChannel, ImageAttentionChannel
from crm.serializers import PersonDetailSerializer
from address.models import Address


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    person = PersonDetailSerializer(read_only=True)
    address = AdressSerializer(read_only=True)
    # TODO studies = http://www.django-rest-framework.org/api-guide/serializers/

    class Meta:
        model = Profile
        fields = '__all__'


class StudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studies
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class CategoryPatologySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPatology
        fields = '__all__'


class PatologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Patology
        fields = '__all__'


class ProfilePatologyOrCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePatologyOrCategory
        fields = '__all__'


class RequestOrderMedicDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestOrderMedicDate
        fields = '__all__'


class ScheduleAttentionChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleAttentionChannel
        fields = '__all__'


class ImageAttentionChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAttentionChannel
        fields = '__all__'
