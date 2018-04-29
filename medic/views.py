from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import Http404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serealizer import ProfileSerializer
# Create your views here.
def index(request):
    return render(request, 'medic/index.html', {})

'''
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
        return render(request, 'medic/profile.html', {'profile': profile, 'studies': studies, 'form': form})
    except Profile.DoesNotExist:
        raise Http404
'''

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,) 


class ProfileListProfile(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = (IsAuthenticated,) # Public APIView
    

