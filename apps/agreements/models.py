from django.db import models
from django.conf import settings
from apps.vehicles.models import Vehicle
from apps.drivers.models import Driver
import datetime


class Agreement(models.Model):
    class ContractType(models.TextChoices):
        SHORT_TERM = 'Short-term Rental', 'Short-term Rental'
        LONG_TERM = 'Long-term Rental', 'Long-term Rental'
        LEASING = 'Leasing', 'Leasing'
        INSTALLMENT = 'Installment (Monthly Payments)', 'Installment (Monthly Payments)'
        BUYOUT = 'Vehicle Buyout', 'Vehicle Buyout'

    class Status(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        COMPLETED = 'Completed', 'Completed'
        PROBLEM = 'Problem', 'Problem'
        CANCELLED = 'Cancelled', 'Cancelled'

    contract_number = models.CharField(max_length=50, unique=True, blank=True)
    contract_type = models.CharField(
        max_length=50,
        choices=ContractType.choices,
        default=ContractType.SHORT_TERM
    )
    
    company_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='agreements'
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.PROTECT,
        related_name='agreements'
    )
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    currency = models.CharField(max_length=10, default='KGS')
    daily_rental_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    deposit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    terms_conditions = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_agreements'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Agreement'
        verbose_name_plural = 'Agreements'

    def __str__(self):
        return f"{self.contract_number} - {self.client_name}"

    def save(self, *args, **kwargs):
        if not self.contract_number:
            year = datetime.date.today().year
            count = Agreement.objects.filter(created_at__year=year).count() + 1
            self.contract_number = f"CONTRACT-{year}-{count:04d}"
        super().save(*args, **kwargs)


class AgreementMedia(models.Model):
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name='media_files'
    )
    file = models.FileField(upload_to='agreements/media/')
    is_before_rental = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        prefix = "Before Rental" if self.is_before_rental else "Additional"
        return f"{prefix} Media for {self.agreement.contract_number}"


class AgreementDocument(models.Model):
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document = models.FileField(upload_to='agreements/documents/')
    category = models.CharField(max_length=100, default='Official Agreement')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} for {self.agreement.contract_number}"
