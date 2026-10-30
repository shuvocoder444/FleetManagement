path = 'apps/site_settings/translations.py'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read().replace('\r\n', '\n')

en_add = """        'menu_team_members': 'Team Members',
        'menu_activity_log': 'Activity Logs',
        'section_team_audit': 'Team & Audit',
"""

ru_add = """        'menu_team_members': 'Сотрудники компании',
        'menu_activity_log': 'Журнал действий',
        'section_team_audit': 'Команда и аудит',
"""

c = c.replace(
    "        'menu_agency_drivers': 'Agency Drivers',\n",
    "        'menu_agency_drivers': 'Agency Drivers',\n" + en_add
)
c = c.replace(
    "        'menu_agency_drivers': 'Водители компании',\n",
    "        'menu_agency_drivers': 'Водители компании',\n" + ru_add
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated translations.py with team & audit keys')
