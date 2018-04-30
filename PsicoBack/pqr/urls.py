from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    url(r'^requestpqr/$', views.requestPQRList.as_view()),
    url(r'^requestpqr-create/$', views.requestPQRCreate.as_view()),
    url(r'^requestpqr/(?P<pk>[0-9]+)/$', views.requestPQRDetail.as_view()),
]
