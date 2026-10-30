path = r'D:\new\templates\dashboard\base_dashboard.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update Company Dashboard link in sidebar
old_company_link = """                    <a href="{% url 'dashboard:admin' %}" 
                       class="flex items-center px-3 {% if request.path == '/dashboard/admin/' %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-chart-pie w-5 {% if request.path == '/dashboard/admin/' %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_company_dashboard }}</span>
                    </a>"""

new_company_link = """                    <a href="{% url 'dashboard:admin' %}" 
                       class="flex items-center px-3 {% if request.path == '/dashboard/admin/' or request.path == '/dashboard/company/' %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-chart-pie w-5 {% if request.path == '/dashboard/admin/' or request.path == '/dashboard/company/' %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_company_dashboard }}</span>
                    </a>"""

# 2. Update Top Switcher Tabs: only show 3 tabs for authenticated Super Admin; for Company Admin show ONLY Fleet Admin pill
old_tabs = """                <!-- 3 DASHBOARD SWITCHER TABS (Live One-Click Switcher) -->
                {% if not request.user.is_authenticated or request.user.is_superuser or request.user.role == 'superadmin' %}
                <div class="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-semibold">
                    <a href="{% url 'dashboard:superadmin' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'superadmin' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-crown text-[10px]"></i>
                        <span>{{ t.tab_superadmin }}</span>
                    </a>
                    <a href="{% url 'dashboard:admin' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'admin' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-building text-[10px]"></i>
                        <span>{{ t.tab_fleetadmin }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'driver' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-id-badge text-[10px]"></i>
                        <span>{{ t.tab_driver }}</span>
                    </a>
                </div>
                {% else %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-red-50 text-red-600 border border-red-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-building text-[11px]"></i>
                        <span>{{ t.tab_fleetadmin|default:'2. Fleet Admin' }}</span>
                    </span>
                </div>
                {% endif %}"""

new_tabs = """                <!-- 3 DASHBOARD SWITCHER TABS (Live One-Click Switcher) -->
                {% if request.user.is_authenticated and (request.user.is_superuser or request.user.role == 'superadmin') %}
                <div class="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-semibold">
                    <a href="{% url 'dashboard:superadmin' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'superadmin' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-crown text-[10px]"></i>
                        <span>{{ t.tab_superadmin }}</span>
                    </a>
                    <a href="{% url 'dashboard:admin' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'admin' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-building text-[10px]"></i>
                        <span>{{ t.tab_fleetadmin }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver' %}" 
                       class="px-2.5 py-1.5 rounded-lg transition flex items-center space-x-1.5 {% if current_dashboard == 'driver' %}bg-white text-red-600 shadow-xs font-bold{% else %}text-slate-600 hover:text-slate-900{% endif %}">
                        <i class="fa-solid fa-id-badge text-[10px]"></i>
                        <span>{{ t.tab_driver }}</span>
                    </a>
                </div>
                {% elif current_dashboard == 'admin' %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-red-50 text-red-600 border border-red-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-building text-[11px]"></i>
                        <span>{{ t.tab_fleetadmin|default:'2. Fleet Admin' }}</span>
                    </span>
                </div>
                {% elif current_dashboard == 'driver' %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-emerald-50 text-emerald-600 border border-emerald-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-id-badge text-[11px]"></i>
                        <span>{{ t.tab_driver|default:'3. Driver Portal' }}</span>
                    </span>
                </div>
                {% else %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-red-50 text-red-600 border border-red-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-crown text-[11px]"></i>
                        <span>{{ t.tab_superadmin|default:'1. Super Admin' }}</span>
                    </span>
                </div>
                {% endif %}"""

# 3. Update User Profile Dropdown Dashboard Link
old_profile_link = """<a href="{% url 'dashboard:index' %}" class="flex items-center px-4 py-2 text-slate-600 hover:bg-slate-50">{{ t.dashboard }}</a>"""
new_profile_link = """<a href="{% if current_dashboard == 'admin' %}{% url 'dashboard:admin' %}{% elif current_dashboard == 'driver' %}{% url 'dashboard:driver' %}{% else %}{% url 'dashboard:superadmin' %}{% endif %}" class="flex items-center px-4 py-2 text-slate-600 hover:bg-slate-50">{{ t.dashboard }}</a>"""

c_norm = c.replace('\r\n', '\n')
c_norm = c_norm.replace(old_company_link.replace('\r\n', '\n'), new_company_link.replace('\r\n', '\n'))
c_norm = c_norm.replace(old_tabs.replace('\r\n', '\n'), new_tabs.replace('\r\n', '\n'))
c_norm = c_norm.replace(old_profile_link.replace('\r\n', '\n'), new_profile_link.replace('\r\n', '\n'))

with open(path, 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("Successfully updated base_dashboard.html")

