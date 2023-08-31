from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
# Create your models here.
class Usertable(AbstractUser):
    email = models.EmailField(primary_key=True, max_length=255)
    full_name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    userrole = models.CharField(default='Author',max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)