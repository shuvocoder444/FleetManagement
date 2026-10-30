with open('templates/landing/base_frontend.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the Dashboard button in desktop navbar directly clickable to dashboard
old_btn = '<button class="flex items-center space-x-2 text-xs sm:text-sm font-bold text-gray-800 bg-gray-100 hover:bg-red-50 hover:text-red-600 px-3.5 py-2 rounded-xl transition border border-gray-200/80 shadow-xs">'
new_btn = '<a href="{% url \'dashboard:index\' %}" class="flex items-center space-x-2 text-xs sm:text-sm font-bold text-gray-800 bg-gray-100 hover:bg-red-50 hover:text-red-600 px-3.5 py-2 rounded-xl transition border border-gray-200/80 shadow-xs">'

assert old_btn in text, "old_btn not found"
text = text.replace(old_btn, new_btn, 1)

# And replace closing </button>
old_btn_close = '<span>{{ t.dashboard }}</span>\n                        <i class="fa-solid fa-chevron-down text-[10px] text-gray-400 group-hover:rotate-180 transition-transform"></i>\n                    </button>'
new_btn_close = '<span>{{ t.dashboard }}</span>\n                        <i class="fa-solid fa-chevron-down text-[10px] text-gray-400 group-hover:rotate-180 transition-transform"></i>\n                    </a>'

text_norm = text.replace('\r\n', '\n')
old_close_norm = old_btn_close.replace('\r\n', '\n')
new_close_norm = new_btn_close.replace('\r\n', '\n')
assert old_close_norm in text_norm, "old_btn_close not found"
text_norm = text_norm.replace(old_close_norm, new_close_norm, 1)

# Add mobile auth section
old_mobile_hdr = '<!-- Mobile Navigation Menu -->\n        <div x-show="mobileNavOpen" x-cloak class="md:hidden border-t border-gray-100 bg-white px-4 py-3 space-y-3">'
new_mobile_hdr = """<!-- Mobile Navigation Menu -->
        <div x-show="mobileNavOpen" x-cloak class="md:hidden border-t border-gray-100 bg-white px-4 py-3 space-y-3">
            {% if request.user.is_authenticated %}
            <div class="p-3 bg-red-50/60 rounded-xl border border-red-100 flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                    <div class="w-8 h-8 rounded-full bg-red-600 text-white flex items-center justify-center text-xs font-bold">
                        {{ request.user.first_name|default:request.user.email|slice:":1"|upper }}
                    </div>
                    <div>
                        <p class="text-xs font-bold text-gray-900">{{ request.user.get_full_name|default:request.user.email }}</p>
                        <p class="text-[10px] text-gray-500 capitalize">{{ request.user.role|default:'User' }}</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <a href="{% url 'dashboard:index' %}" class="px-3 py-1.5 bg-red-600 text-white font-bold text-xs rounded-lg shadow-xs">
                        {{ t.dashboard }}
                    </a>
                    <a href="{% url 'accounts:logout' %}" class="px-2.5 py-1.5 bg-rose-100 text-rose-700 font-bold text-xs rounded-lg hover:bg-rose-200">
                        <i class="fa-solid fa-arrow-right-from-bracket"></i>
                    </a>
                </div>
            </div>
            {% else %}
            <div class="flex items-center space-x-2 pt-1">
                <a href="{% url 'accounts:login' %}" class="flex-1 py-2 text-center text-xs font-bold text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-lg">
                    {{ t.sign_in|default:'Login' }}
                </a>
                <a href="{% url 'accounts:register' %}" class="flex-1 py-2 text-center text-xs font-bold text-white bg-red-600 hover:bg-red-700 rounded-lg shadow-xs">
                    {{ t.register|default:'Register' }}
                </a>
            </div>
            {% endif %}"""

old_mobile_norm = old_mobile_hdr.replace('\r\n', '\n')
new_mobile_norm = new_mobile_hdr.replace('\r\n', '\n')
assert old_mobile_norm in text_norm, "old_mobile_hdr not found"
text_norm = text_norm.replace(old_mobile_norm, new_mobile_norm, 1)

with open('templates/landing/base_frontend.html', 'w', encoding='utf-8') as f:
    f.write(text_norm)

print("Updated base_frontend.html with clickable dashboard button and mobile auth card")

