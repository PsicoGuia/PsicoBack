from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signupmedic/$', views.signupMedic, name='signupmedic'),
    url(r'^loginmedic/$', views.loginMedic, name='loginmedic'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^person/$', views.PersonList.as_view(),
        name="person-list"),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view(),
        name='person-detail'),
    url(r'^user/$', views.UserList.as_view(),
        name="user-list"),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
