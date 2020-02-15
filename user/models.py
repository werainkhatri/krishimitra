from django.db import models
from django.contrib.auth import models as auth_models


class CustomUserManager(auth_models.BaseUserManager):
    def create_user(self, contact, password, email, name, active=0, is_staff=False,
                    is_superuser=False):
        if not contact:
            raise ValueError("Users must have a contact number")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            contact=contact,
            email=self.normalize_email(email),
            active=active,
            name=name,
            password=password,
            is_superuser=is_superuser,
            is_staff = is_superuser
        )
        user.set_password(password)  # change user password
        user.active = active
        user.save(using=self._db)
        return user

    def create_superuser(self, contact, password, email, name):
        user = self.create_user(
            contact=contact,
            email=email,
            name=name,
            password=password,
            is_superuser=True,
            is_staff = True
        )
        return user


class BaseUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USER_TYPE = (
        ('ADM', 'Admin'),
        ('FMR', 'Farmer'),
        ('SPL', 'Supplier'),
        ('RTL', 'Retailer'),
        ('LLD', 'Landlord'),
    )
    ACTIVE_STATUS = (
        (-1, 'NOT ACTIVE'),
        (0, 'NEW USER'),
        (1, 'ACTIVE'),
    )
    user_type = models.CharField(
        max_length=3, choices=USER_TYPE, default='ADM', null=True, blank=True)
    contact = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    state = models.CharField(max_length=32)

    active = models.IntegerField(choices=ACTIVE_STATUS, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['email', 'name']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        super(BaseUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "BaseUser"
        verbose_name_plural = "BaseUsers"

    def __str__(self):
        return self.contact
