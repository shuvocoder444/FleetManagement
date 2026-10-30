import os, re

files = [
    r'D:\new\apps\agreements\views.py',
    r'D:\new\apps\vehicles\views.py',
    r'D:\new\apps\drivers\views.py',
    r'D:\new\apps\billing\views.py',
    r'D:\new\apps\accounts\views.py',
    r'D:\new\apps\site_settings\views.py',
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Add import if needed
    if 'get_active_dashboard_role' not in c:
        c = 'from apps.site_settings.context_processors import get_active_dashboard_role\n' + c
    
    # Replace the hardcoded fallback
    c = c.replace(
        "request.session.get('active_dashboard_role', 'superadmin')",
        "get_active_dashboard_role(request)"
    )
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated {p}!')

print('ALL VIEWS UPDATED WITH get_active_dashboard_role!')
