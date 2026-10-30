with open('templates/dashboard/base_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = "{% if display_user.company_name %}{{ display_user.company_name }}{% elif display_user.role == 'individual' %}Personal{% else %}Company{% endif %}"
new_logic = "{% if display_user.get_company_account.company_name %}{{ display_user.get_company_account.company_name }}{% elif display_user.company_name %}{{ display_user.company_name }}{% elif display_user.role == 'individual' %}Personal{% else %}Company{% endif %}"

text = text.replace(old_logic, new_logic)

with open('templates/dashboard/base_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('templates/dashboard/admin.html', 'r', encoding='utf-8') as f:
    admin_text = f.read()

admin_text = admin_text.replace(old_logic, new_logic)

with open('templates/dashboard/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_text)

print("Updated company badge logic across base_dashboard.html and admin.html")
