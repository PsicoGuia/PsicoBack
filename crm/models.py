from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
from address.models import AddressField

'''
At the time no additional user information has been used, but I know that I will be doing it
'''
def Person(User):
    phone = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"