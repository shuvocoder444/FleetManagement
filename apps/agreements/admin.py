from django.contrib import admin
from .models import Agreement, AgreementMedia, AgreementDocument


class AgreementMediaInline(admin.TabularInline):
    model = AgreementMedia
    extra = 1


class AgreementDocumentInline(admin.TabularInline):
    model = AgreementDocument
    extra = 1


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ('contract_number', 'client_name', 'contract_type', 'vehicle', 'driver', 'start_date', 'end_date', 'status', 'created_by')
    list_filter = ('contract_type', 'status', 'start_date')
    search_fields = ('contract_number', 'client_name', 'company_name', 'vehicle__title', 'driver__first_name', 'driver__last_name')
    inlines = [AgreementMediaInline, AgreementDocumentInline]
