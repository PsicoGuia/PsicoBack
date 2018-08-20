from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from django.conf import settings

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance

from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import status
from rest_framework import filters
from rest_framework import pagination
import django_filters.rest_framework


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
    ImageAttentionChannelSerializer, ProfileLiteSerializer

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


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    max_page_size = 1000


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = ProfileLiteSerializer
        self.queryset = Profile.objects.filter(person__user=request.user)
        self.permission_classes = (permissions.IsAuthenticated,)
        return self.partial_update(request, *args, **kwargs)


class ProfileMyListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        """Returns Polls that belong to the current user"""
        return Profile.objects.filter(person__user=self.request.user)


class ProfilesFilter(django_filters.FilterSet):
    patology__in = django_filters.BaseInFilter(
        field_name='profilepatologyorcategory__patology_id', distinct=True,
        lookup_expr='in')
   
    class Meta:
        model = Profile
        # get defaults fields + custom
        fields = [obj.attname for obj in Profile._meta.fields
                  if obj.attname not in [
                      'picture',
                      'personalDocumentFile',
                      'professionalCardFile',
                      'position']]


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    pagination_class = StandardResultsSetPagination
    filter_class = ProfilesFilter

    def get_queryset(self):
        # Get nearest profiles
        lat = self.request.query_params.get("lat", None)
        lng = self.request.query_params.get("lng", None)
        max_distance = self.request.query_params.get(
            "max_distance", settings.POST_GIS_MAX_DISTANCE_SEARCH)
        if not lat or not lng:
            return Profile.objects.all()
        position = GEOSGeometry('POINT(%s %s)' % (lng, lat), srid=4326)
        return Profile.objects.filter(position__distance_lte=(
            position, D(km=max_distance)
        )).annotate(distance=Distance('position', position)) \
            .order_by('distance')


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


class CategoryPatologyListView(generics.ListAPIView):
    queryset = CategoryPatology.objects.all()
    serializer_class = CategoryPatologySerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (authentication.TokenAuthentication,)


class CategoryPatologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryPatology.objects.all()
    serializer_class = CategoryPatologySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class PatologyListView(generics.ListAPIView):
    queryset = Patology.objects.all()
    serializer_class = PatologySerializer


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
