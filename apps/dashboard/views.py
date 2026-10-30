from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.accounts.models import CustomUser
from apps.vehicles.models import Vehicle
from apps.drivers.models import Driver, DriverHistory, DriverRating
from apps.agreements.models import Agreement
from apps.billing.models import Subscription, ManualPayment, Plan
from django.db.models import Sum


def dashboard_router(request):
    """Smart router: routes user to their appropriate dashboard based on their role."""
    user = request.user

    # 1. Authenticated user's real role takes strict priority
    if user.is_authenticated:
        if getattr(user, 'role', '') == CustomUser.Role.DRIVER:
            request.session['active_dashboard_role'] = 'driver'
            request.session.modified = True
            return redirect('dashboard:driver')
        elif getattr(user, 'role', '') in [CustomUser.Role.COMPANY, CustomUser.Role.ADMIN, CustomUser.Role.INDIVIDUAL]:
            request.session['active_dashboard_role'] = 'admin'
            request.session.modified = True
            return redirect('dashboard:admin')
        elif user.is_superuser or getattr(user, 'role', '') == CustomUser.Role.SUPERADMIN:
            active_role = request.session.get('active_dashboard_role')
            if active_role == 'admin':
                return redirect('dashboard:admin')
            elif active_role == 'driver':
                return redirect('dashboard:driver')
            return redirect('dashboard:superadmin')

    # 2. Unauthenticated / guest preview
    active_role = request.session.get('active_dashboard_role')
    if active_role == 'driver':
        return redirect('dashboard:driver')
    elif active_role == 'superadmin':
        return redirect('dashboard:superadmin')
    return redirect('dashboard:admin')


def superadmin_dashboard(request):
    """1. Super Admin Master Dashboard"""
    # Guard: If logged in as driver, redirect to driver dashboard
    if request.user.is_authenticated and getattr(request.user, 'role', '') == CustomUser.Role.DRIVER:
        request.session['active_dashboard_role'] = 'driver'
        return redirect('dashboard:driver')

    # Guard: If logged in as company, redirect to company admin
    if request.user.is_authenticated and not (request.user.is_superuser or getattr(request.user, 'role', '') == CustomUser.Role.SUPERADMIN):
        request.session['active_dashboard_role'] = 'admin'
        return redirect('dashboard:admin')

    request.session['active_dashboard_role'] = 'superadmin'
    request.session.modified = True
    display_user = request.user if request.user.is_authenticated else CustomUser.objects.filter(role=CustomUser.Role.SUPERADMIN).first()

    # Subscriber Metrics
    total_subscribers = CustomUser.objects.filter(role__in=[CustomUser.Role.INDIVIDUAL, CustomUser.Role.COMPANY]).count()
    active_subscribers = Subscription.objects.filter(status=Subscription.Status.ACTIVE).values('user').distinct().count()
    pending_approval = Subscription.objects.filter(status=Subscription.Status.PENDING).count() + ManualPayment.objects.filter(status=ManualPayment.Status.PENDING).count()
    one_time_orders = Subscription.objects.filter(plan__interval=Plan.Interval.ONCE).count()

    # Platform Contracts & Revenue
    total_contracts = Agreement.objects.count()
    active_contracts = Agreement.objects.filter(status=Agreement.Status.ACTIVE).count()
    payments_received = ManualPayment.objects.filter(status=ManualPayment.Status.APPROVED).aggregate(total=Sum('amount'))['total'] or 2623.50

    # Vehicles Fleet
    vehicles_available = Vehicle.objects.filter(status=Vehicle.Status.AVAILABLE).count()
    vehicles_rented = Vehicle.objects.filter(status=Vehicle.Status.RENTED).count()
    vehicles_leased = Vehicle.objects.filter(status=Vehicle.Status.LEASED).count()
    vehicles_maintenance = Vehicle.objects.filter(status=Vehicle.Status.MAINTENANCE).count()
    total_vehicles = Vehicle.objects.count()

    # Drivers
    drivers_total = Driver.objects.count()
    drivers_busy = Driver.objects.filter(status=Driver.Status.BUSY).count()
    drivers_available = Driver.objects.filter(status=Driver.Status.AVAILABLE).count()
    drivers_bad = Driver.objects.filter(status=Driver.Status.WARNING).count()

    # Recent lists
    recent_agreements = Agreement.objects.select_related('vehicle', 'driver').order_by('-created_at')[:5]
    recent_drivers = Driver.objects.order_by('-created_at')[:5]
    pending_payments = ManualPayment.objects.filter(status=ManualPayment.Status.PENDING).order_by('-created_at')[:5]

    context = {
        'display_user': display_user,
        'current_dashboard': 'superadmin',
        
        # Metrics
        'total_subscribers': total_subscribers,
        'active_subscribers': active_subscribers,
        'pending_approval': pending_approval,
        'one_time_orders': one_time_orders,

        'total_contracts': total_contracts,
        'active_contracts': active_contracts,
        'payments_received': payments_received,

        'vehicles_available': vehicles_available,
        'vehicles_rented': vehicles_rented,
        'vehicles_leased': vehicles_leased,
        'vehicles_maintenance': vehicles_maintenance,
        'total_vehicles': total_vehicles,

        'drivers_total': drivers_total,
        'drivers_busy': drivers_busy,
        'drivers_available': drivers_available,
        'drivers_bad': drivers_bad,

        'recent_agreements': recent_agreements,
        'recent_drivers': recent_drivers,
        'pending_payments': pending_payments,
    }
    return render(request, 'dashboard/superadmin.html', context)


def admin_dashboard(request):
    """2. Rental Company / Fleet Admin Dashboard (like Team JBDIT)"""
    # Guard: If logged in as driver, redirect to driver dashboard!
    if request.user.is_authenticated and getattr(request.user, 'role', '') == CustomUser.Role.DRIVER:
        request.session['active_dashboard_role'] = 'driver'
        return redirect('dashboard:driver')

    request.session['active_dashboard_role'] = 'admin'
    request.session.modified = True
    display_user = request.user if request.user.is_authenticated else CustomUser.objects.filter(role=CustomUser.Role.COMPANY).first()

    # Filter data for this company / fleet
    vehicles = Vehicle.objects.all()
    if display_user and not display_user.is_superadmin:
        my_vehicles = vehicles.filter(created_by=display_user)
        if not my_vehicles.exists():
            my_vehicles = vehicles
    else:
        my_vehicles = vehicles

    total_fleet = my_vehicles.count()
    fleet_available = my_vehicles.filter(status=Vehicle.Status.AVAILABLE).count()
    fleet_rented = my_vehicles.filter(status=Vehicle.Status.RENTED).count()
    fleet_maintenance = my_vehicles.filter(status=Vehicle.Status.MAINTENANCE).count()

    # My Agreements
    my_agreements = Agreement.objects.select_related('vehicle', 'driver').order_by('-created_at')
    active_rentals = my_agreements.filter(status=Agreement.Status.ACTIVE).count()
    completed_rentals = my_agreements.filter(status=Agreement.Status.COMPLETED).count()

    # Drivers under company
    my_drivers = Driver.objects.all()
    drivers_count = my_drivers.count()
    drivers_available = my_drivers.filter(status=Driver.Status.AVAILABLE).count()

    # Subscription status
    my_subscription = Subscription.objects.filter(user=display_user, status=Subscription.Status.ACTIVE).first() if display_user else None

    context = {
        'display_user': display_user,
        'current_dashboard': 'admin',
        'company_name': display_user.company_name if display_user and display_user.company_name else 'Team JBDIT Rental Ltd',

        'total_fleet': total_fleet,
        'fleet_available': fleet_available,
        'fleet_rented': fleet_rented,
        'fleet_maintenance': fleet_maintenance,

        'active_rentals': active_rentals,
        'completed_rentals': completed_rentals,
        'total_contracts': my_agreements.count(),

        'drivers_count': drivers_count,
        'drivers_available': drivers_available,

        'my_subscription': my_subscription,
        'recent_agreements': my_agreements[:5],
        'my_vehicles': my_vehicles[:6],
    }
    return render(request, 'dashboard/admin.html', context)


def driver_dashboard(request):
    """3. Driver Dedicated Portal Dashboard"""
    request.session['active_dashboard_role'] = 'driver'
    request.session.modified = True
    display_user = request.user if request.user.is_authenticated else CustomUser.objects.filter(role=CustomUser.Role.DRIVER).first()

    # Fetch driver model
    driver = None
    if display_user and hasattr(display_user, 'driver_profile'):
        driver = display_user.driver_profile
    if not driver:
        # Match driver by email
        if display_user and display_user.email:
            driver = Driver.objects.filter(email=display_user.email).first()
    if not driver:
        driver = Driver.objects.first()

    # Driver statistics
    agreements = Agreement.objects.filter(driver=driver) if driver else Agreement.objects.none()
    active_agreement = agreements.filter(status=Agreement.Status.ACTIVE).first()
    history_entries = driver.history_entries.all() if driver else []
    ratings = driver.ratings.all() if driver else []

    context = {
        'display_user': display_user,
        'driver': driver,
        'current_dashboard': 'driver',

        'total_agreements': agreements.count(),
        'active_agreements': agreements.filter(status=Agreement.Status.ACTIVE).count(),
        'completed_agreements': agreements.filter(status=Agreement.Status.COMPLETED).count(),
        'problem_agreements': agreements.filter(status=Agreement.Status.PROBLEM).count(),
        'total_issues': len(history_entries),
        'completion_rate': 100 if agreements.count() == 0 else int((agreements.filter(status=Agreement.Status.COMPLETED).count() / agreements.count()) * 100),
        'total_reviews': len(ratings),
        'average_rating': driver.average_rating if driver else 4.8,

        'active_agreement': active_agreement,
        'history_entries': history_entries,
        'ratings': ratings,
    }
    return render(request, 'dashboard/driver.html', context)
