from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djmoney.models.fields import MoneyField
#from geoposition.fields import GeopositionField
from address.models import AddressField

from django.contrib.gis.db.models import PointField

def profileFilePath(instance, filename):
    return 'medic/files/profiles/{0}/{1}'.format(instance.user.id, filename)

def attentionChannelFilePath(instance, filename):
    return 'medic/files/attentionchanels/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=profileFilePath, default='/static/images/no_user.png')
    MALE = 'M'
    FEMALE = 'F'
    UNDEF = 'U'
    GENRES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
        (UNDEF, 'No definido'),
    )
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=UNDEF,
    )
    CEDULA_CIUDADANIA = 'CC'
    CEDULA_EXTRANJERIA = 'CE'
    PASAPORTE = 'PS'
    DOCUMENT_TYPES = (
        (CEDULA_CIUDADANIA, 'Cedula de ciudadania'),
        (CEDULA_EXTRANJERIA, 'Cedula de extranjeria'),
        (PASAPORTE, 'Pasaporte'),
    )
    personalDocumentType = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=DOCUMENT_TYPES,
        default=CEDULA_CIUDADANIA,
    )
    personalDocumentNumber = models.BigIntegerField('Numero de documento', null=True)
    personalDocumentFile = models.ImageField(upload_to=profileFilePath, null=True)
    professionalCardNumber = models.CharField(max_length=25, null=True)
    professionalCardFile = models.ImageField(upload_to=profileFilePath, null=True)

    city = models.CharField(max_length=25, null=True)
    address = AddressField(blank=True, null=True, on_delete=models.CASCADE)
    position = PointField(geography=False, null=True, blank=True, default='POINT(0.0 0.0)')

    cost = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='COP',
        max_digits=11,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.get_username()

'''
All user haven´t group MEDIC
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

'''
def studiesFilePath(instance, filename):
    return 'medic/files/{0}/{1}'.format(instance.profile.user.id, filename)

class Studies(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    BACHELOR = 'BH'
    CERTIFICAION = 'CR'
    SPECIALIZATION = 'SP'
    MASTER = 'MS'
    DOCTOR = 'PH'
    DEGREE = (
        (BACHELOR, 'Pregrado'),
        (CERTIFICAION, 'Certificacion'),
        (SPECIALIZATION, 'Especializacion'),
        (MASTER, 'Maestria'),
        (DOCTOR, 'Doctorado'),
    )
    level = models.CharField(
        max_length=2,
        choices=DEGREE,
        default=BACHELOR,
    )
    title = models.CharField(max_length=100)
    date = models.DateField()
    experienceYears = models.IntegerField()
    file = models.FileField(upload_to=studiesFilePath)
    certificated = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def getLevel(self):
        return dict(self.DEGREE)[self.level]
    def getUserName(self):
        return self.profile.user.get_username()
    def __unicode__(self):
        return '%s - %s: %s'%(self.getUserName(), self.getLevel(), self.title)

class ScheduleAttentionChannel(models.Model):
    # 0- None, 1-Monday, 5-Monday and Wendesday
    #attention_channel = models.ForeignKey(AttentionChannel, on_delete=models.CASCADE)
    bitDays = models.IntegerField()
    duration = models.DurationField() #TODO CHECK
    
    class Meta:
        verbose_name = "Horario de canal de atención"
        verbose_name_plural = "Horarios de canal de atención"


class ImageAttentionChannel(models.Model):
    #attention_channel = models.ForeignKey(AttentionChannel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=profileFilePath)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 

class AttentionChannel(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    schedules = models.ManyToManyField(ScheduleAttentionChannel)
    images = models.ManyToManyField(ImageAttentionChannel)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Office(AttentionChannel):
    description = models.TextField(null=True, blank=True)
    position = PointField(geography=False, null=True, blank=True)

    class Meta:
        verbose_name = "Consultorio"
        verbose_name_plural = "Consultorios"


   


class Chat(AttentionChannel):
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Consultorio"
        verbose_name_plural = "Consultorios"

class CategoryPatology(models.Model):
    name = models.TextField(null=False, blank=False)
    #categoryFather = models.ForeignKey(CategoryPatology, on_delete=models.CASCADE, null=True, blank=True)  #DEPRECATED

    class Meta:
        verbose_name = "Categoria de Patologías"
        verbose_name_plural = "Categorias de Patologías"

class Patology(models.Model):
    name = models.TextField(null=False, blank=False)
    category = models.ForeignKey(CategoryPatology, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = "Patología"
        verbose_name_plural = "Patologías"

class ProfilePatologyOrCategory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    patology = models.ForeignKey(Patology, on_delete=models.CASCADE, null=True, blank=True) #Dinamical assign and filter
    category = models.ForeignKey(CategoryPatology, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = "Patología o categoría del perfil"
        verbose_name_plural = "Patologías o categorías del perfil"

class RequestOrderMedicDate(models.Model):
    name_pacient = models.TextField()
    age_pacient = models.IntegerField()
    patology_pacient = models.ForeignKey(Patology, on_delete=models.SET_NULL,null=True)
    adicional_description_pacient = models.TextField()
    email_pacient = models.TextField()
    phone = models.TextField()
    
    class Meta:
        verbose_name = "Petición de cita medica"
        verbose_name_plural = "Peticiones de cita medica"