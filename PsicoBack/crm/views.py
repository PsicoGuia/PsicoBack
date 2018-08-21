from django.contrib.auth import login, authenticate
from django.http import Http404
from address.models import Address
from django.http import HttpResponse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import Http404, HttpResponse, JsonResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import status
from rest_framework import filters

from .models import GROUP_MEDIC, Person
from django.contrib.auth.models import User
from .serializers import PersonSerializer, PersonDetailSerializer, UserLiteSerializer, UserSerializer
from medic.models import Profile

from django.conf import settings

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


@api_view(['POST'])
def signupMedic(request):
    JSONResponse = {}
    if request.method == 'POST':
        # try:
        # print(request.POST)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        identification_number = request.data.get('identification_number', None)
        profesional_number = request.data.get('profesional_number', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)
        phone = request.data.get('phone', None)
        term = request.data.get('version_terms', None)
        terms_abusdata = request.data.get('version_terms_abeusdata', None)
        notification = request.data.get('notification', None)
        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()
        person = Person(user=user, phone=phone, term=term,
                        term_abausdata=terms_abusdata, notification=notification)
        person.save()
        group, created = Group.objects.get_or_create(name=GROUP_MEDIC)
        group.user_set.add(person.user)
        prof = Profile(
            person=person, personalDocumentNumber=identification_number)
        prof.save()

        # Send Email
        mail_subject = 'Activate your account.'
        message = render_to_string('email_confirm_account.html', {
            'person': person,
            'domain': settings.DOMAIN,
            'uid': urlsafe_base64_encode(force_bytes(person.user.pk)).decode(),
            'token': account_activation_token.make_token(person.user),
        })
        to_email = email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        JSONResponse = {
            'person': PersonDetailSerializer(person).data,
            'domain': settings.DOMAIN,
            'uid': urlsafe_base64_encode(force_bytes(person.user.pk)).decode(),
            'token': account_activation_token.make_token(person.user),
            'msg': 'Please confirm your email\
         address to complete the registration',
        }
        return Response(JSONResponse)
    # catch e as Exception:
    #    print(e)
    else:
        return HttpResponseForbidden()

@api_view(['POST'])
def loginMedic(request):
    if request.method == 'POST':
        try:
            JSONResponse ={}
            email = request.data['email']
            password = request.data['password']
            user = User.objects.filter(email=email).first()
            if not user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            authorizated = user.check_password(password)
        
            if not authorizated:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        
            if (not user.groups.filter(name=GROUP_MEDIC).exists()):
                Response(status=status.HTTP_401_UNAUTHORIZED)    
            
            token, created = Token.objects.get_or_create(user=user)
            JSONResponse['key'] = token.key
            JSONResponse['person'] = PersonDetailSerializer(Person.objects.filter(user=user).first()).data
            return Response(JSONResponse)
            
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        return HttpResponseForbidden()


class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)


class PersonDetail(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonDetailSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = PersonSerializer
        self.queryset = Person.objects.filter(user=request.user)
        self.permission_classes = (permissions.IsAuthenticated,)
        return self.partial_update(request, *args, **kwargs)    

class UserList(generics.ListAPIView):
    queryset = User.objects.none()
    serializer_class = PersonSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = UserLiteSerializer
        self.queryset = User.objects.filter(pk=request.user.id)
        self.permission_classes = (permissions.IsAuthenticated,)
        return self.partial_update(request, *args, **kwargs)    



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')