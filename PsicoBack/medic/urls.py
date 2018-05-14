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
from . import views

API_VERSION = '1.0'

urlpatterns = [
    path(r'profile/', views.ProfileListView.as_view(),
         name="profile-list"),
    path(r'profile/<int:pk>/', views.ProfileDetailView.as_view(),
         name='profile-detail'),
    path(r'studies/', views.StudiesListView.as_view(),
         name="studies-list"),
    path(r'studies/<int:pk>/', views.StudiesDetailView.as_view(),
         name='studies-detail'),
    path(r'office/', views.OfficeListView.as_view(),
         name="office-list"),
    path(r'office/<int:pk>/', views.OfficeDetailView.as_view(),
         name='office-detail'),
    path(r'chat/', views.ChatListView.as_view(),
         name="chat-list"),
    path(r'chat/<int:pk>/', views.ChatDetailView.as_view(),
         name='chat-detail'),
    path(r'categoryPatology/', views.CategoryPatologyListView.as_view(),
         name="categoryPatology-list"),
    path(r'categoryPatology/<int:pk>/', views.CategoryPatologyDetailView.as_view(),
         name='categoryPatology-detail'),
    path(r'patology/', views.PatologyListView.as_view(),
         name="patology-list"),
    path(r'patology/<int:pk>/', views.PatologyDetailView.as_view(),
         name='patology-detail'),
    path(r'profilePatologyOrCategory/', views.ProfilePatologyOrCategoryListView.as_view(),
         name="profilePatologyOrCategory-list"),
    path(r'profilePatologyOrCategory/<int:pk>/', views.ProfilePatologyOrCategoryDetailView.as_view(),
         name='profilePatologyOrCategory-detail'),
    path(r'requestOrderMedicDate/', views.RequestOrderMedicDateListView.as_view(),
         name="requestOrderMedicDate-list"),
    path(r'requestOrderMedicDate/<int:pk>/', views.RequestOrderMedicDateDetailView.as_view(),
         name='requestOrderMedicDate-detail'),
    path(r'scheduleAttentionChannel/', views.RequestOrderMedicDateListView.as_view(),
         name="scheduleAttentionChannel-list"),
    path(r'scheduleAttentionChannel/<int:pk>/', views.ScheduleAttentionChannelDetailView.as_view(),
         name='scheduleAttentionChannel-detail'),
    path(r'imageAttentionChannel/', views.ImageAttentionChannelListView.as_view(),
         name="imageAttentionChannel-list"),
    path(r'imageAttentionChannel/<int:pk>/', views.ImageAttentionChannelDetailView.as_view(),
         name='imageAttentionChannel-detail'),
]
