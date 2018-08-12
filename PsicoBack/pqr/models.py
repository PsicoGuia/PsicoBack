from django.db import models
from medic.models import Profile, RequestOrderMedicDate
# Create your models here.


class requestPQR(models.Model):

    name_request_user = models.TextField()
    email_request_user = models.TextField()
    phone_request_user = models.TextField()
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    request_order = models.ForeignKey(
        RequestOrderMedicDate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Petición PQR"
        verbose_name_plural = "Peticiones PQR"

    def __str__(self):
        return str(self.email_request_user)


class FAQ(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return str(self.title)
