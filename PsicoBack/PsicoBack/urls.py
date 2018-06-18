"""PsicoBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import password_reset, \
    password_reset_done, password_reset_confirm, password_reset_complete

API_VERSION = '1.0'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/'+API_VERSION+'/rest-auth/', include('rest_auth.urls')),
    path(r'api/'+API_VERSION+'/pqr/', include('pqr.urls')),
    path(r'api/'+API_VERSION+'/crm/', include('crm.urls')),
    path(r'api/'+API_VERSION+'/medic/', include('medic.urls')),
    url(
        regex=r'password_reset/$',
        view=password_reset,
        name='password_reset'
    ),
    url(
        regex=r'password_reset/done/$',
        view=password_reset_done,
        name='password_reset_done'
    ),
    url(
        regex=r'new_password/(?P<uidb64>[0-9A-Za-z_\-]+)'
              r'/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=password_reset_confirm,
        name='password_reset_confirm'
    ),
    url(
        regex=r'contrib/reset/done/$',
        view=password_reset_complete,
        name='password_reset_complete'
    ),
]
