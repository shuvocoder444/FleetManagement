# 1. Update templates/landing/base_frontend.html
with open(r'D:\new\templates\landing\base_frontend.html', 'r', encoding='utf-8') as f:
    fe = f.read().replace('\r\n', '\n')

old_fe_msg = """    <!-- Flash Messages -->
    {% if messages %}
    <div class="fixed top-20 right-5 z-50 space-y-2 max-w-md w-full">
        {% for message in messages %}
        <div class="p-4 rounded-xl shadow-xl flex items-center justify-between text-white text-sm font-semibold {% if message.tags == 'error' %}bg-rose-600{% elif message.tags == 'warning' %}bg-amber-600{% else %}bg-emerald-600{% endif %}">
            <div class="flex items-center space-x-2.5">
                <i class="fa-solid {% if message.tags == 'error' %}fa-circle-exclamation{% else %}fa-circle-check{% endif %}"></i>
                <span>{{ message }}</span>
            </div>
            <button onclick="this.parentElement.remove()" class="ml-3 text-white/80 hover:text-white text-lg">&times;</button>
        </div>
        {% endfor %}
    </div>
    {% endif %}"""

new_fe_msg = """    <!-- Flash Messages (Auto-dismissing) -->
    {% if messages %}
    <div class="fixed top-24 right-5 z-50 space-y-2 max-w-md w-full pointer-events-none">
        {% for message in messages %}
        <div x-data="{ show: true }" 
             x-show="show" 
             x-init="setTimeout(() => show = false, 4000)"
             x-transition:leave="transition ease-in duration-300"
             x-transition:leave-start="opacity-100 transform translate-y-0"
             x-transition:leave-end="opacity-0 transform -translate-y-2"
             class="pointer-events-auto p-4 rounded-xl shadow-xl flex items-center justify-between text-white text-sm font-semibold {% if message.tags == 'error' %}bg-rose-600{% elif message.tags == 'warning' %}bg-amber-600{% else %}bg-emerald-600{% endif %}">
            <div class="flex items-center space-x-2.5">
                <i class="fa-solid {% if message.tags == 'error' %}fa-circle-exclamation{% else %}fa-circle-check{% endif %}"></i>
                <span>{{ message }}</span>
            </div>
            <button @click="show = false" class="ml-3 text-white/80 hover:text-white text-lg leading-none">&times;</button>
        </div>
        {% endfor %}
    </div>
    {% endif %}"""

fe = fe.replace(old_fe_msg, new_fe_msg)
with open(r'D:\new\templates\landing\base_frontend.html', 'w', encoding='utf-8') as f:
    f.write(fe)
print("Updated base_frontend.html")

# 2. Update templates/dashboard/base_dashboard.html
with open(r'D:\new\templates\dashboard\base_dashboard.html', 'r', encoding='utf-8') as f:
    db = f.read().replace('\r\n', '\n')

old_body = '<body class="h-full flex overflow-hidden" x-data="{ mobileSidebarOpen: false }">'
new_body = """<body class="h-full flex overflow-hidden" x-data="{ mobileSidebarOpen: false }">

    <!-- Flash Messages (Auto-dismissing in Dashboard) -->
    {% if messages %}
    <div class="fixed top-5 right-5 z-50 space-y-2 max-w-md w-full pointer-events-none">
        {% for message in messages %}
        <div x-data="{ show: true }" 
             x-show="show" 
             x-init="setTimeout(() => show = false, 4000)"
             x-transition:leave="transition ease-in duration-300"
             x-transition:leave-start="opacity-100 transform translate-y-0"
             x-transition:leave-end="opacity-0 transform -translate-y-2"
             class="pointer-events-auto p-3.5 rounded-xl shadow-xl flex items-center justify-between text-white text-xs sm:text-sm font-semibold {% if message.tags == 'error' %}bg-rose-600{% elif message.tags == 'warning' %}bg-amber-600{% else %}bg-emerald-600{% endif %}">
            <div class="flex items-center space-x-2.5">
                <i class="fa-solid {% if message.tags == 'error' %}fa-circle-exclamation{% else %}fa-circle-check{% endif %}"></i>
                <span>{{ message }}</span>
            </div>
            <button @click="show = false" class="ml-3 text-white/80 hover:text-white text-lg leading-none">&times;</button>
        </div>
        {% endfor %}
    </div>
    {% endif %}"""

db = db.replace(old_body, new_body)
with open(r'D:\new\templates\dashboard\base_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(db)
print("Updated base_dashboard.html")

# 3. Update apps/accounts/views.py
with open(r'D:\new\apps\accounts\views.py', 'r', encoding='utf-8') as f:
    av = f.read().replace('\r\n', '\n')

old_logout = """def logout_view(request):
    if request.user.is_authenticated:
        log_activity(
            request,
            ActivityLog.ActionType.LOGIN,
            ActivityLog.Module.AUTH,
            f"Logged out of system",
            company=request.user.get_company_account()
        )
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
    # Clear any previous unread messages from session/storage so they don't bleed into the landing page
    from django.contrib.messages import get_messages
    storage = get_messages(request)
    for _ in storage:
        pass
    storage.used = True

    auth_logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('landing_page')"""

old_login_user = """            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)"""

new_login_user = """            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Clear previous unread messages if any
                from django.contrib.messages import get_messages
                storage = get_messages(request)
                for _ in storage:
                    pass
                storage.used = True

                auth_login(request, user)"""

av = av.replace(old_logout, new_logout)
av = av.replace(old_login_user, new_login_user)

with open(r'D:\new\apps\accounts\views.py', 'w', encoding='utf-8') as f:
    f.write(av)
print("Updated apps/accounts/views.py")

