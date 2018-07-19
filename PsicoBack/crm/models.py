from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

'''
At the time no additional user information has been used,
but I know that I will be doing it
'''
GROUP_MEDIC = "MEDICS"


class Person(models.Model):
    # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person',
        unique=True,
        null=True,
    )
    phone = models.TextField(null=True, blank=True)
    term = models.FloatField(null=True, blank=True)
    term_abausdata = models.FloatField(null=True, blank=True)
    notification = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return str(self.user)

