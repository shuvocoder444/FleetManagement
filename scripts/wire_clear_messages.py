path = r'D:\new\apps\accounts\views.py'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

clear_helper = """def clear_messages(request):
    \"\"\"Clears any stale or accumulated unread messages from session/cookie storage.\"\"\"
    try:
        from django.contrib.messages import get_messages
        storage = get_messages(request)
        if hasattr(storage, '_queued_messages'):
            storage._queued_messages.clear()
        for s in getattr(storage, 'storages', []):
            if hasattr(s, '_queued_messages'):
                s._queued_messages.clear()
            if hasattr(s, '_loaded_data'):
                s._loaded_data = []
    except Exception:
        pass


@csrf_exempt"""

c = c.replace('@csrf_exempt', clear_helper, 1)

# Now in logout_view
old_logout = """def logout_view(request):
    if request.user.is_authenticated:
        log_activity(
            request,
            ActivityLog.ActionType.LOGIN,
            ActivityLog.Module.AUTH,
            f"Logged out of system",
            company=request.user.get_company_account()
        )
    # Clear any previous unread messages from session/storage so they don't bleed into the landing page
    from django.contrib.messages import get_messages
    storage = get_messages(request)
    for _ in storage:
        pass
    storage.used = True

    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('landing_page')"""

new_logout = """def logout_view(request):
    if request.user.is_authenticated:
        log_activity(
            request,
            ActivityLog.ActionType.LOGIN,
            ActivityLog.Module.AUTH,
            f"Logged out of system",
            company=request.user.get_company_account()
        )
    # Wipe any accumulated messages from previous dashboard actions
    clear_messages(request)

    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('landing_page')"""

c = c.replace(old_logout, new_logout)

# In login_view
old_login_clean = """                # Clear previous unread messages if any
                from django.contrib.messages import get_messages
                storage = get_messages(request)
                for _ in storage:
                    pass
                storage.used = True"""

new_login_clean = """                # Clear previous unread messages if any
                clear_messages(request)"""

c = c.replace(old_login_clean, new_login_clean)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated apps/accounts/views.py with clear_messages helper!')

