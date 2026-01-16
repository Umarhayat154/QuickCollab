from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManger(BaseUserManager):
    def create_user(self, email, name=None, password=None, role=None):
        if not email:
            raise ValueError("Please User must be login with Email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)
        user.set_password(password)
        user.is_active(True)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, role="author")
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    Roles = [
        ("author", "Author"),
        ("reader", "Reader"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    roles = models.CharField(choices=Roles, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects=UserManger()

    def __str__(self):
        return self.email