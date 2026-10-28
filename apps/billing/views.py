from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import ManualPayment, Subscription, Plan


def manual_payments_list(request):
    status_filter = request.GET.get('status', '').strip()
    payments = ManualPayment.objects.all()
    if status_filter:
        payments = payments.filter(status=status_filter)

    pending_count = ManualPayment.objects.filter(status=ManualPayment.Status.PENDING).count()
    approved_count = ManualPayment.objects.filter(status=ManualPayment.Status.APPROVED).count()
    cancelled_count = ManualPayment.objects.filter(status=ManualPayment.Status.CANCELLED).count()

    context = {
        'payments': payments,
        'status_filter': status_filter,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'cancelled_count': cancelled_count,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'billing/manual_payments.html', context)


def approve_payment(request, pk):
    payment = get_object_or_404(ManualPayment, pk=pk)
    payment.status = ManualPayment.Status.APPROVED
    payment.reviewed_at = timezone.now()
    if request.user.is_authenticated:
        payment.reviewed_by = request.user
    payment.save()

    # Automatically activate or extend subscription
    Subscription.objects.create(
        user=payment.user,
        plan=payment.plan,
        start_date=timezone.now(),
        end_date=timezone.now() + timezone.timedelta(days=30),
        status=Subscription.Status.ACTIVE
    )
    messages.success(request, f'Payment #{payment.id} has been approved and subscription activated!')
    return redirect('billing:manual_payments')


def reject_payment(request, pk):
    payment = get_object_or_404(ManualPayment, pk=pk)
    payment.status = ManualPayment.Status.CANCELLED
    payment.reviewed_at = timezone.now()
    if request.user.is_authenticated:
        payment.reviewed_by = request.user
    payment.save()
    messages.warning(request, f'Payment #{payment.id} marked as rejected.')
    return redirect('billing:manual_payments')


def subscriptions_list(request):
    status_filter = request.GET.get('status', '').strip()
    subscriptions = Subscription.objects.all()
    if status_filter:
        subscriptions = subscriptions.filter(status=status_filter)

    total_count = Subscription.objects.count()
    active_count = Subscription.objects.filter(status=Subscription.Status.ACTIVE).count()
    pending_count = Subscription.objects.filter(status=Subscription.Status.PENDING).count()

    context = {
        'subscriptions': subscriptions,
        'status_filter': status_filter,
        'total_count': total_count,
        'active_count': active_count,
        'pending_count': pending_count,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'billing/subscriptions.html', context)


def plans_list(request):
    plans = Plan.objects.all()
    context = {
        'plans': plans,
        'current_dashboard': 'superadmin' if request.user.is_superuser or getattr(request.user, 'role', '') == 'superadmin' else 'admin',
    }
    return render(request, 'billing/plans.html', context)
