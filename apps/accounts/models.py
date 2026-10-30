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

    # Multi-user Team & Seat Management:
    # Individual = 1 user max. Company = 1 Owner + up to 2 Team Members (Total 3 seats).
    company = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='team_members',
        help_text="Parent company account if this user is a staff/team member."
    )
    member_role = models.CharField(max_length=50, default='Owner', blank=True)

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

    def get_company_account(self):
        """Returns the primary company account (either self if owner, or self.company if team member)."""
        if self.company:
            return self.company
        return self

    @property
    def is_company_owner(self):
        return self.role == self.Role.COMPANY and self.company is None

    @property
    def team_seat_count(self):
        """Current number of active seats used (1 for owner + active team members)."""
        company = self.get_company_account()
        return 1 + company.team_members.filter(is_active=True).count()

    @property
    def max_allowed_seats(self):
        """Individual = 1 seat. Company = 3 seats."""
        if self.role == self.Role.INDIVIDUAL:
            return 1
        return 3

    @property
    def seats_available(self):
        return max(0, self.max_allowed_seats - self.team_seat_count)


class ActivityLog(models.Model):
    class Module(models.TextChoices):
        VEHICLES = 'vehicles', 'Vehicles'
        AGREEMENTS = 'agreements', 'Rental Agreements'
        DRIVERS = 'drivers', 'Drivers & Verification'
        BILLING = 'billing', 'Subscription & Billing'
        TEAM = 'team', 'Team Management'
        AUTH = 'auth', 'Authentication'

    class ActionType(models.TextChoices):
        CREATE = 'create', 'Created'
        UPDATE = 'update', 'Updated'
        DELETE = 'delete', 'Deleted'
        VERIFY = 'verify', 'Verified'
        LOGIN = 'login', 'Logged In'

    company = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='activity_logs'
    )
    actor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='performed_activities'
    )
    actor_name = models.CharField(max_length=255)
    actor_email = models.EmailField(blank=True, null=True)
    actor_role = models.CharField(max_length=50, default='Owner')

    action_type = models.CharField(max_length=20, choices=ActionType.choices, default=ActionType.CREATE)
    module = models.CharField(max_length=30, choices=Module.choices, default=Module.AGREEMENTS)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activity Logs'

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.actor_name}: {self.description}"
