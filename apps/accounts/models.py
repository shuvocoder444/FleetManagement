from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', CustomUser.Role.SUPERADMIN)
        extra_fields.setdefault('status', CustomUser.Status.VERIFIED)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = 'superadmin', 'Super Admin'
        ADMIN = 'admin', 'Admin'
        COMPANY = 'company', 'Rental Company'
        DRIVER = 'driver', 'Driver'
        INDIVIDUAL = 'individual', 'Individual'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Verification Pending'
        VERIFIED = 'verified', 'Verified'
        SUSPENDED = 'suspended', 'Suspended'

    username = None
    email = models.EmailField('Email Address', unique=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.COMPANY)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    # Company / Business Information
    company_name = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    business_registration_number = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        full_name = self.get_full_name()
        return f"{full_name} ({self.email})" if full_name else self.email

    @property
    def is_superadmin(self):
        return self.role == self.Role.SUPERADMIN or self.is_superuser

    @property
    def is_admin(self):
        return self.role in [self.Role.SUPERADMIN, self.Role.ADMIN, self.Role.COMPANY]

    @property
    def is_driver(self):
        return self.role == self.Role.DRIVER
