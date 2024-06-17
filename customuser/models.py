from django.db import models

# Create your models here.
from django.utils import timezone # type: ignore
from django.utils.translate import gettext_lazy as _ # type: ignore
class MyUser(models.Model):
    email = models.EmailField(_("Email address"), max_length=254,unique=True)
    username = models.CharField(_("Username"), max_length=150,unique=True)
    first_name = models.CharField(_("First name"), max_length=150)
    start_date = models.DateTimeField(default=timezone.now, null=True)
    about = models.TextField(_("About"), max_length=500,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    