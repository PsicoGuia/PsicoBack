from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import status
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import parser_classes, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Profile, Studies, Office, Chat,\
    CategoryPatology, Patology, ProfilePatologyOrCategory,\
    RequestOrderMedicDate, ScheduleAttentionChannel, ImageAttentionChannel
from .serealizer import ProfileSerializer, StudiesSerializer, \
    OfficeSerializer, ChatSerializer, CategoryPatologySerializer, \
    PatologySerializer, ProfilePatologyOrCategorySerializer, \
    RequestOrderMedicDateSerializer, ScheduleAttentionChannelSerializer, \
    ImageAttentionChannelSerializer

# Create your views here.

'''
def index(request):
    return render(request, 'medic/index.html', {})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'medic/signup.html', {'form': form})

def profile(request, username):
    try:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                print(':.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.')
                print(request.POST)
                print(form)
        profile = Profile.objects.get(user__username=username)
        print('profile id')
        print(profile.id)
        studies = Studies.objects.filter(profile__id=profile.id)
        print(profile.location)
        form = ProfileForm()
        return render(request, 'medic/profile.html', {'profile': profile,
        'studies': studies, 'form': form})
    except Profile.DoesNotExist:
        raise Http404
'''


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class StudiesListView(generics.ListCreateAPIView):
    queryset = Studies.objects.all()
    serializer_class = StudiesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class StudiesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studies.objects.all()
    serializer_class = StudiesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class OfficeListView(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class OfficeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ChatListView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ChatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class CategoryPatologyListView(generics.ListCreateAPIView):
    queryset = CategoryPatology.objects.all()
    serializer_class = CategoryPatologySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class CategoryPatologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryPatology.objects.all()
    serializer_class = CategoryPatologySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class PatologyListView(generics.ListCreateAPIView):
    queryset = Patology.objects.all()
    serializer_class = PatologySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class PatologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patology.objects.all()
    serializer_class = PatologySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ProfilePatologyOrCategoryListView(generics.ListCreateAPIView):
    queryset = ProfilePatologyOrCategory.objects.all()
    serializer_class = ProfilePatologyOrCategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ProfilePatologyOrCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfilePatologyOrCategory.objects.all()
    serializer_class = ProfilePatologyOrCategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class RequestOrderMedicDateListView(generics.ListCreateAPIView):
    queryset = RequestOrderMedicDate.objects.all()
    serializer_class = RequestOrderMedicDateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class RequestOrderMedicDateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestOrderMedicDate.objects.all()
    serializer_class = RequestOrderMedicDateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ScheduleAttentionChannelListView(generics.ListCreateAPIView):
    queryset = ScheduleAttentionChannel.objects.all()
    serializer_class = ScheduleAttentionChannelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ScheduleAttentionChannelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleAttentionChannel.objects.all()
    serializer_class = ScheduleAttentionChannelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ImageAttentionChannelListView(generics.ListCreateAPIView):
    queryset = ImageAttentionChannel.objects.all()
    serializer_class = ImageAttentionChannelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class ImageAttentionChannelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageAttentionChannel.objects.all()
    serializer_class = ImageAttentionChannelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
