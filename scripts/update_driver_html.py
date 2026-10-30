with open('templates/dashboard/driver.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace active-car header
old_car_hdr = """                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center space-x-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        <h3 class="text-sm font-bold text-slate-900">{{ t.current_assigned_vehicle }}</h3>
                    </div>
                    <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-100 font-bold text-slate-700">
                        {{ active_agreement.contract_number }}
                    </span>
                </div>"""

new_car_hdr = """                <div class="flex items-center justify-between mb-4">
                    <div class="flex items-center space-x-2">
                        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        <h3 class="text-sm font-bold text-slate-900">{{ t.current_assigned_vehicle }}</h3>
                    </div>
                    <div class="flex items-center space-x-2">
                        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-100 font-bold text-slate-700">
                            {{ active_agreement.contract_number }}
                        </span>
                        <a href="{% url 'dashboard:driver_vehicle' %}" class="text-xs font-bold text-red-600 hover:text-red-700 hover:underline inline-flex items-center">
                            Full Details <i class="fa-solid fa-arrow-right ml-1 text-[10px]"></i>
                        </a>
                    </div>
                </div>"""

# Replace history-records header
old_hist_hdr = """                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-sm font-bold text-slate-900">{{ t.incident_history_log }}</h3>
                    <span class="text-[11px] text-slate-400">{{ history_entries|length }} {{ t.records_logged }}</span>
                </div>"""

new_hist_hdr = """                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-sm font-bold text-slate-900">{{ t.incident_history_log }}</h3>
                    <div class="flex items-center space-x-3">
                        <span class="text-[11px] text-slate-400">{{ history_entries|length }} {{ t.records_logged }}</span>
                        <a href="{% url 'dashboard:driver_history' %}" class="text-xs font-bold text-red-600 hover:text-red-700 hover:underline inline-flex items-center">
                            View All <i class="fa-solid fa-arrow-right ml-1 text-[10px]"></i>
                        </a>
                    </div>
                </div>"""

text_norm = text.replace('\r\n', '\n')
old_car_hdr_norm = old_car_hdr.replace('\r\n', '\n')
new_car_hdr_norm = new_car_hdr.replace('\r\n', '\n')
old_hist_hdr_norm = old_hist_hdr.replace('\r\n', '\n')
new_hist_hdr_norm = new_hist_hdr.replace('\r\n', '\n')

assert old_car_hdr_norm in text_norm, 'old_car_hdr not found!'
text_norm = text_norm.replace(old_car_hdr_norm, new_car_hdr_norm)

assert old_hist_hdr_norm in text_norm, 'old_hist_hdr not found!'
text_norm = text_norm.replace(old_hist_hdr_norm, new_hist_hdr_norm)

with open('templates/dashboard/driver.html', 'w', encoding='utf-8') as f:
    f.write(text_norm)

print('Successfully updated driver.html')
