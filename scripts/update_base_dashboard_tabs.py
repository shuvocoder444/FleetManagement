path = r'D:\new\templates\dashboard\base_dashboard.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

target = """                <!-- 3 DASHBOARD SWITCHER TABS (Live One-Click Switcher) -->
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
                </div>"""

replacement = """                <!-- 3 DASHBOARD SWITCHER TABS (Live One-Click Switcher) -->
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

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
print('Found:', target_norm in c_norm)
c_norm = c_norm.replace(target_norm, replacement)
with open(path, 'w', encoding='utf-8') as f:
    f.write(c_norm)
print('Updated base_dashboard.html!')
