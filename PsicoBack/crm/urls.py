from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signupmedic/$', views.signupMedic, name='signupmedic'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    
    url(r'^person/$', views.PersonList.as_view(), name='logout'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view(), name='logout'),
]
    