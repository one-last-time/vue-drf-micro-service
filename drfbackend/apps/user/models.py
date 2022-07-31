from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class AccountTypes(models.IntegerChoices):
    Admin = 1
    Vendor = 2
    Customer = 3


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    username = models.CharField(_('Username'), max_length=60, blank=False, null=False)
    user_type = models.IntegerField(_('User Type'), choices=AccountTypes.choices, default=3, blank=False, null=False)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('last Name'), max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = UserManager()

    def __str__(self):
        return self.email