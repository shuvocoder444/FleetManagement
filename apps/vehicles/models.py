from django.db import models
from django.conf import settings


class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        RENT = 'Rent', 'Rent'
        LEASE = 'Lease', 'Lease'

    class Status(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        RENTED = 'Rented', 'Rented'
        LEASED = 'Leased', 'Leased'
        MAINTENANCE = 'Maintenance', 'Maintenance'

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    vehicle_type = models.CharField(max_length=20, choices=VehicleType.choices, default=VehicleType.RENT)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.AVAILABLE)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='vehicles/covers/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return f"{self.title} - {self.brand} {self.model} ({self.year})"


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='vehicles/gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.vehicle.title}"


class VehicleDocument(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='vehicles/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.vehicle.title}"
