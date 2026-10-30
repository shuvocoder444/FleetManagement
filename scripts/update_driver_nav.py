with open('templates/dashboard/base_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_sec = """                    <a href="{% url 'dashboard:driver' %}#active-car" class="flex items-center px-3 py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50">
                        <i class="fa-solid fa-car-side w-5 text-slate-400"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_current_vehicle }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver' %}#agreements-list" class="flex items-center px-3 py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50">
                        <i class="fa-regular fa-file-lines w-5 text-slate-400"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_trip_contracts }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver' %}#history-records" class="flex items-center px-3 py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50">
                        <i class="fa-solid fa-clock-rotate-left w-5 text-slate-400"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_incident_history }}</span>
                    </a>"""

new_sec = """                    <a href="{% url 'dashboard:driver_vehicle' %}" 
                       class="flex items-center px-3 {% if request.path == '/dashboard/driver/vehicle/' %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-car-side w-5 {% if request.path == '/dashboard/driver/vehicle/' %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_current_vehicle }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver_agreements' %}" 
                       class="flex items-center px-3 {% if request.path == '/dashboard/driver/agreements/' %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-regular fa-file-lines w-5 {% if request.path == '/dashboard/driver/agreements/' %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_trip_contracts }}</span>
                    </a>
                    <a href="{% url 'dashboard:driver_history' %}" 
                       class="flex items-center px-3 {% if request.path == '/dashboard/driver/history/' %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-clock-rotate-left w-5 {% if request.path == '/dashboard/driver/history/' %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_incident_history }}</span>
                    </a>"""

text_norm = text.replace('\r\n', '\n')
old_sec_norm = old_sec.replace('\r\n', '\n')
new_sec_norm = new_sec.replace('\r\n', '\n')

if old_sec_norm in text_norm:
    updated = text_norm.replace(old_sec_norm, new_sec_norm)
    with open('templates/dashboard/base_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(updated)
    print("Successfully replaced driver navigation in base_dashboard.html")
else:
    print("Could not find old_sec_norm!")

