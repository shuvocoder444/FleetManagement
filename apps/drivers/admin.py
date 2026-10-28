from django.contrib import admin
from .models import Driver, DriverHistory, DriverRating


class DriverHistoryInline(admin.TabularInline):
    model = DriverHistory
    extra = 1


class DriverRatingInline(admin.TabularInline):
    model = DriverRating
    extra = 0
    readonly_fields = ('created_at',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'passport_number', 'personal_id', 'status', 'average_rating', 'created_by')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'passport_number', 'license_number', 'personal_id')
    inlines = [DriverHistoryInline, DriverRatingInline]


@admin.register(DriverHistory)
class DriverHistoryAdmin(admin.ModelAdmin):
    list_display = ('driver', 'history_type', 'incident_date', 'reported_by')
    list_filter = ('history_type', 'incident_date')
    search_fields = ('driver__first_name', 'driver__last_name', 'driver__passport_number', 'description')
