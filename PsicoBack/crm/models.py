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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='person',
        unique=True,
        null=True,
    )
    phone = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
