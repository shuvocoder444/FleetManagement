from django.contrib import admin
from .models import WebsiteSetting, Currency, ContactMessage, FrontendPage


@admin.register(WebsiteSetting)
class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'contact_phone')


@admin.register(FrontendPage)
class FrontendPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'badge', 'is_active', 'updated_at')
    list_filter = ('is_active', 'updated_at')
    search_fields = ('title', 'subtitle', 'section_title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol', 'exchange_rate', 'is_base', 'is_active')
    list_filter = ('is_base', 'is_active')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)

