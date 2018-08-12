from rest_framework import serializers
from .models import Profile, Studies, Office, Chat, HomeVisit,\
    CategoryPatology, Patology, ProfilePatologyOrCategory,\
    RequestOrderMedicDate, ScheduleAttentionChannel, ImageAttentionChannel,\
    AttentionChannel
from crm.serializers import PersonDetailSerializer
from address.models import Address


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class StudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studies
        fields = '__all__'

class CategoryPatologySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPatology
        fields = '__all__'


class PatologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Patology
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


class AttentionChannelSerializer(serializers.ModelSerializer):
    images = ImageAttentionChannelSerializer(many=True, read_only=True)
    schedules = ScheduleAttentionChannelSerializer(many=True, read_only=True)
    
    class Meta:
        model = AttentionChannel
        fields = '__all__'


class OfficeSerializer(AttentionChannelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class ChatSerializer(AttentionChannelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class HomeVisitSerializer(AttentionChannelSerializer):
    class Meta:
        model = HomeVisit
        fields = '__all__'        


class ProfilePatologyOrCategorySerializer(serializers.ModelSerializer):
    patology = PatologySerializer(read_only=True)
    category = CategoryPatologySerializer(read_only=True)
    
    class Meta:
        model = ProfilePatologyOrCategory
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    person = PersonDetailSerializer(read_only=True)
    address = AdressSerializer(read_only=True)
    studies_set = StudiesSerializer(many=True, read_only=True)
    homevisit_set = HomeVisitSerializer(many=True, read_only=True)
    office_set = OfficeSerializer(many=True, read_only=True)
    chat_set = ChatSerializer(many=True, read_only=True)
    profilepatologyorcategory_set = ProfilePatologyOrCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileLiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'
