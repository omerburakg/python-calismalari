from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext

# Create your models here.


class User(AbstractUser):
    bio = models.TextField(gettext("biograph"), null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth Date")
