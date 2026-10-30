path = r'D:\new\templates\dashboard\base_dashboard.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

target = """            <div>
                <p class="px-3 text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2">{{ t.section_my_account }}</p>"""

team_section = """            <div>
                <p class="px-3 text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2">{{ t.section_team_audit|default:'Team & Audit' }}</p>
                <nav class="space-y-1">
                    <a href="{% url 'accounts:team' %}" 
                       class="flex items-center px-3 {% if '/accounts/team/' in request.path %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-users-gear w-5 {% if '/accounts/team/' in request.path %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_team_members|default:'Team Members' }}</span>
                        <span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded bg-blue-50 text-blue-600">3 Seats</span>
                    </a>
                    <a href="{% url 'accounts:activity_log' %}" 
                       class="flex items-center px-3 {% if '/accounts/activity-log/' in request.path %}py-2.5 text-xs font-bold rounded-xl text-red-600 bg-red-50/80 border border-red-100/50 shadow-xs{% else %}py-2 text-xs font-medium rounded-xl text-slate-700 hover:text-red-600 hover:bg-slate-50 transition{% endif %}">
                        <i class="fa-solid fa-clock-rotate-left w-5 {% if '/accounts/activity-log/' in request.path %}text-red-600 text-sm{% else %}text-slate-400{% endif %}"></i>
                        <span class="ml-2.5 flex-1">{{ t.menu_activity_log|default:'Activity Logs' }}</span>
                        <span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded bg-red-100 text-red-600">Audit</span>
                    </a>
                </nav>
            </div>

            <div>
                <p class="px-3 text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2">{{ t.section_my_account }}</p>"""

c = c.replace(target, team_section)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated base_dashboard.html with Team & Audit section!')
