from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from models import Profile, Studies
from django.http import Http404
from address.models import Address

from forms import SignUpForm, ProfileForm

