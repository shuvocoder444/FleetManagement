# Update base_dashboard.html
with open('templates/dashboard/base_dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_menu = '<span class="ml-2.5 flex-1">Buy Subscription</span>'
new_menu = '<span class="ml-2.5 flex-1">{{ t.menu_buy_subscription|default:t.buy_subscription|default:\'Buy Subscription\' }}</span>'

assert old_menu in text, "old_menu not found in base_dashboard.html"
text = text.replace(old_menu, new_menu)

with open('templates/dashboard/base_dashboard.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated base_dashboard.html")

# Update subscriptions.html
with open('templates/billing/subscriptions.html', 'r', encoding='utf-8') as f:
    sub_text = f.read()

old_sub_btn = '<i class="fa-solid fa-credit-card mr-2"></i> Buy Subscription'
new_sub_btn = '<i class="fa-solid fa-credit-card mr-2"></i> {{ t.menu_buy_subscription|default:t.buy_subscription|default:\'Buy Subscription\' }}'

if old_sub_btn in sub_text:
    sub_text = sub_text.replace(old_sub_btn, new_sub_btn)
    with open('templates/billing/subscriptions.html', 'w', encoding='utf-8') as f:
        f.write(sub_text)
    print("Updated subscriptions.html")
