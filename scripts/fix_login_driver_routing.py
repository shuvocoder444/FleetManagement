path = r'D:\new\apps\accounts\views.py'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

old_block = """@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Clear previous unread messages if any
                clear_messages(request)

                auth_login(request, user)
                if getattr(user, 'role', '') in [CustomUser.Role.COMPANY, CustomUser.Role.ADMIN, CustomUser.Role.INDIVIDUAL]:
                    request.session['active_dashboard_role'] = 'admin'
                elif getattr(user, 'role', '') == CustomUser.Role.DRIVER:
                    request.session['active_dashboard_role'] = 'driver'
                else:
                    request.session['active_dashboard_role'] = 'superadmin'

                log_activity(
                    request,
                    ActivityLog.ActionType.LOGIN,
                    ActivityLog.Module.AUTH,
                    f"Logged into system",
                    company=user.get_company_account()
                )

                messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                if next_url:
                    return redirect(next_url)
                return redirect('dashboard:index')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')"""

new_block = """@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        if getattr(request.user, 'role', '') == CustomUser.Role.DRIVER:
            return redirect('dashboard:driver')
        elif getattr(request.user, 'role', '') in [CustomUser.Role.COMPANY, CustomUser.Role.ADMIN, CustomUser.Role.INDIVIDUAL]:
            return redirect('dashboard:admin')
        return redirect('dashboard:superadmin')

    next_url = request.GET.get('next') or request.POST.get('next') or ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '').strip()

        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                clear_messages(request)
                auth_login(request, user)

                # Route strictly according to authenticated user's role
                if getattr(user, 'role', '') == CustomUser.Role.DRIVER:
                    request.session['active_dashboard_role'] = 'driver'
                    request.session.modified = True
                    log_activity(
                        request,
                        ActivityLog.ActionType.LOGIN,
                        ActivityLog.Module.AUTH,
                        f"Driver logged into dedicated portal",
                        company=user.get_company_account()
                    )
                    messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                    return redirect('dashboard:driver')

                elif getattr(user, 'role', '') in [CustomUser.Role.COMPANY, CustomUser.Role.ADMIN, CustomUser.Role.INDIVIDUAL]:
                    request.session['active_dashboard_role'] = 'admin'
                    request.session.modified = True
                    log_activity(
                        request,
                        ActivityLog.ActionType.LOGIN,
                        ActivityLog.Module.AUTH,
                        f"Logged into company portal",
                        company=user.get_company_account()
                    )
                    messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                    if next_url and '/driver/' not in next_url:
                        return redirect(next_url)
                    return redirect('dashboard:admin')

                else:
                    request.session['active_dashboard_role'] = 'superadmin'
                    request.session.modified = True
                    log_activity(
                        request,
                        ActivityLog.ActionType.LOGIN,
                        ActivityLog.Module.AUTH,
                        f"Superadmin logged into system",
                        company=user.get_company_account()
                    )
                    messages.success(request, f'Welcome back, {user.first_name or user.email}!')
                    if next_url:
                        return redirect(next_url)
                    return redirect('dashboard:superadmin')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')"""

c = c.replace(old_block, new_block)
with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated login_view in apps/accounts/views.py!')
