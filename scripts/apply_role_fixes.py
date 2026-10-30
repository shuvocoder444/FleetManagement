# 1. Update translations.py
with open('apps/site_settings/translations.py', 'r', encoding='utf-8') as f:
    trans_content = f.read()

# Replace tab_fleetadmin and fleet_badge in EN
trans_content = trans_content.replace("'tab_fleetadmin': '2. Fleet Admin'", "'tab_fleetadmin': '2. Company'")
trans_content = trans_content.replace("'fleet_badge': 'Fleet Company'", "'fleet_badge': 'Company'")

# Replace tab_fleetadmin and fleet_badge in RU
trans_content = trans_content.replace("'tab_fleetadmin': '2. Автопарк'", "'tab_fleetadmin': '2. Компания'")
trans_content = trans_content.replace("'fleet_badge': 'Автопарк'", "'fleet_badge': 'Компания'")

with open('apps/site_settings/translations.py', 'w', encoding='utf-8') as f:
    f.write(trans_content)
print("Updated translations.py")

# 2. Update base_dashboard.html
with open('templates/dashboard/base_dashboard.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Replace logo link to active dashboard instead of landing_page
old_logo = '<a href="{% url \'landing_page\' %}" class="flex items-center space-x-2.5">'
new_logo = '<a href="{% if current_dashboard == \'superadmin\' %}{% url \'dashboard:superadmin\' %}{% elif current_dashboard == \'driver\' %}{% url \'dashboard:driver\' %}{% else %}{% url \'dashboard:admin\' %}{% endif %}" class="flex items-center space-x-2.5">'
assert old_logo in base_html, "old_logo not found"
base_html = base_html.replace(old_logo, new_logo, 1)

# Replace sidebar brand badge
old_badge = """                    <span class="text-[9px] uppercase tracking-widest font-bold text-slate-400">
                        {% if current_dashboard == 'superadmin' %}{{ t.superadmin_badge }}
                        {% elif current_dashboard == 'admin' %}{{ t.fleet_badge }}
                        {% else %}{{ t.driver_badge }}{% endif %}
                    </span>"""

new_badge = """                    <span class="text-[9px] uppercase tracking-widest font-bold text-slate-400">
                        {% if current_dashboard == 'superadmin' %}{{ t.superadmin_badge }}
                        {% elif current_dashboard == 'admin' %}
                            {% if display_user.company_name %}{{ display_user.company_name }}{% elif display_user.role == 'individual' %}Personal{% else %}Company{% endif %}
                        {% else %}{{ t.driver_badge }}{% endif %}
                    </span>"""

base_html_norm = base_html.replace('\r\n', '\n')
old_badge_norm = old_badge.replace('\r\n', '\n')
new_badge_norm = new_badge.replace('\r\n', '\n')
assert old_badge_norm in base_html_norm, "old_badge not found"
base_html_norm = base_html_norm.replace(old_badge_norm, new_badge_norm, 1)

# Replace footer role badge
old_footer_badge = """                    <p class="text-[10px] text-slate-500 capitalize">
                        {% if current_dashboard == 'superadmin' %}{{ t.superadmin_badge }}
                        {% elif current_dashboard == 'admin' %}{{ t.fleet_badge }}
                        {% else %}{{ t.driver_badge }}{% endif %}
                    </p>"""

new_footer_badge = """                    <p class="text-[10px] text-slate-500 capitalize">
                        {% if current_dashboard == 'superadmin' %}{{ t.superadmin_badge }}
                        {% elif current_dashboard == 'admin' %}
                            {% if display_user.company_name %}{{ display_user.company_name }}{% elif display_user.role == 'individual' %}Personal{% else %}Company{% endif %}
                        {% else %}{{ t.driver_badge }}{% endif %}
                    </p>"""

old_footer_norm = old_footer_badge.replace('\r\n', '\n')
new_footer_norm = new_footer_badge.replace('\r\n', '\n')
assert old_footer_norm in base_html_norm, "old_footer_badge not found"
base_html_norm = base_html_norm.replace(old_footer_norm, new_footer_norm, 1)

# Replace top navbar admin pill
old_admin_pill = """                {% elif current_dashboard == 'admin' %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-red-50 text-red-600 border border-red-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-building text-[11px]"></i>
                        <span>{{ t.tab_fleetadmin|default:'2. Fleet Admin' }}</span>
                    </span>
                </div>"""

new_admin_pill = """                {% elif current_dashboard == 'admin' %}
                <div class="flex items-center space-x-2">
                    <span class="px-3 py-1.5 rounded-xl bg-red-50 text-red-600 border border-red-100 font-bold text-xs flex items-center space-x-1.5">
                        <i class="fa-solid fa-building text-[11px]"></i>
                        <span>
                            {% if display_user.company_name %}
                                {{ display_user.company_name }}
                            {% elif display_user.role == 'individual' %}
                                Personal
                            {% else %}
                                Company
                            {% endif %}
                        </span>
                    </span>
                </div>"""

old_admin_norm = old_admin_pill.replace('\r\n', '\n')
new_admin_norm = new_admin_pill.replace('\r\n', '\n')
assert old_admin_norm in base_html_norm, "old_admin_pill not found"
base_html_norm = base_html_norm.replace(old_admin_norm, new_admin_norm, 1)

# Add Website link before language switcher in top navbar
old_curr_btn = '<!-- Currency Selector -->'
new_curr_btn = """<!-- Visit Public Website in new tab -->
                <a href="{% url 'landing_page' %}" target="_blank" title="Visit Website in new tab"
                   class="hidden md:flex items-center space-x-1.5 px-3 py-1.5 rounded-xl text-xs font-bold text-slate-600 hover:text-red-600 bg-slate-100 hover:bg-slate-200 transition">
                    <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                    <span>Website</span>
                </a>

                <!-- Currency Selector -->"""

assert old_curr_btn in base_html_norm, "old_curr_btn not found"
base_html_norm = base_html_norm.replace(old_curr_btn, new_curr_btn, 1)

with open('templates/dashboard/base_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(base_html_norm)
print("Updated base_dashboard.html")

# 3. Update dashboard/admin.html welcome badge
with open('templates/dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

old_welcome_badge = '<span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase bg-emerald-100 text-emerald-700">{{ t.fleet_badge }}</span>'
new_welcome_badge = """<span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase bg-emerald-100 text-emerald-700">
                {% if display_user.company_name %}{{ display_user.company_name }}{% elif display_user.role == 'individual' %}Personal{% else %}Company{% endif %}
            </span>"""

assert old_welcome_badge in admin_html, "old_welcome_badge not found"
admin_html = admin_html.replace(old_welcome_badge, new_welcome_badge, 1)

with open('templates/dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
print("Updated dashboard/admin.html")
