from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import status
from rest_framework import filters

from .models import requestPQR
from .serializers import requestPQRSerializer, requestPQRDetailSerializer
# Create your views here.

class requestPQRCreate(generics.CreateAPIView):
    queryset = requestPQR.objects.all()
    serializer_class = requestPQRSerializer
    # Public endPoint
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAuthenticated,)


class requestPQRList(generics.ListAPIView):
    queryset = requestPQR.objects.all()
    serializer_class = requestPQRSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class requestPQRDetail(generics.RetrieveUpdateAPIView):
    queryset = requestPQR.objects.all()
    serializer_class = requestPQRDetailSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
