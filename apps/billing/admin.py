from django.contrib import admin
from .models import Plan, Subscription, ManualPayment


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'interval', 'status')
    list_filter = ('interval', 'status')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'plan')
    search_fields = ('user__email', 'plan__name')


@admin.register(ManualPayment)
class ManualPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'amount', 'currency', 'payment_method', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('user__email', 'plan__name')
