from django.contrib import admin
from .models import Vehicle, VehicleImage, VehicleDocument


class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1


class VehicleDocumentInline(admin.TabularInline):
    model = VehicleDocument
    extra = 1


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'vehicle_type', 'brand', 'model', 'year', 'registration_number', 'status', 'created_by')
    list_filter = ('vehicle_type', 'status', 'brand', 'year')
    search_fields = ('title', 'brand', 'model', 'registration_number')
    inlines = [VehicleImageInline, VehicleDocumentInline]
