from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode   
from django.template.loader import render_to_string 
from django.core.mail import EmailMessage
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from .models import GROUP_MEDIC, Person
from .serializers import PersonSerializer


from django.conf import settings

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()


#add appi decorator
def signupMedic(request):
    if request.method == 'POST':
    #try:
        name = request.POST['name']
        identification_number = request.POST['identification_number']
        profesional_number = request.POST['profesional_number']
        email = request.POST['email']
        phone = request.POST['phone']
        password =  request.POST['password']
        person = Person.objects.create_user(email, email, password)
        person.first_name = name
        person.is_active = False
        group, created = Group.objects.get_or_create(name=GROUP_MEDIC)
        group.user_set.add(person)
        person.save()
        
        # Send Email
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'person': person,
            'domain': settings.DOMAIN,
            'uid':urlsafe_base64_encode(force_bytes(person.pk)),
            'token':account_activation_token.make_token(person),
        })
        to_email = email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        
        return HttpResponse('Please confirm your email address to complete the registration')        
    #catch e as Exception:
    #    print(e)
    else:
        return HttpResponseForbidden()

def loginMedic(request):
    if request.method == 'POST':
        email = request.POST['email']
        password =  request.POST['password']
        user = authenticate(username=email, password=password)
        
        if user.group_set.filter(name=GROUP_MEDIC).exists():
            token, created = Token.objects.get_or_create(user=user)
            person = Person.objects.get(username=email)
            return JsonResponse({"token":token,
                            "person":PersonSerializer(person).data,})
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()
    


