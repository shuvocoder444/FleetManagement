path = r'D:\new\templates\users\register.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old_pass = """<input type="password" name="password" required placeholder="{{ t.placeholder_password|default:'Create a strong password' }}"
                                       class="w-full pl-10 pr-4 py-2.5 text-xs sm:text-sm rounded-xl border border-slate-200 focus:ring-2 focus:ring-red-500/20 focus:border-red-500 outline-none transition bg-white text-slate-800 font-medium">"""

new_pass = """<input type="password" id="id_reg_password" name="password" required placeholder="{{ t.placeholder_password|default:'Create a strong password' }}"
                                       class="w-full pl-10 pr-10 py-2.5 text-xs sm:text-sm rounded-xl border border-slate-200 focus:ring-2 focus:ring-red-500/20 focus:border-red-500 outline-none transition bg-white text-slate-800 font-medium">
                                <button type="button" 
                                        onclick="const inp = document.getElementById('id_reg_password'); const icon = this.querySelector('i'); if (inp.type === 'password') { inp.type = 'text'; icon.classList.remove('fa-eye'); icon.classList.add('fa-eye-slash'); } else { inp.type = 'password'; icon.classList.remove('fa-eye-slash'); icon.classList.add('fa-eye'); }"
                                        class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-600 focus:outline-none transition cursor-pointer" 
                                        title="Show / Hide Password">
                                    <i class="fa-solid fa-eye text-sm"></i>
                                </button>"""

old_conf = """<input type="password" name="confirm_password" required placeholder="{{ t.placeholder_confirm_password|default:'Confirm your password' }}"
                                       class="w-full pl-10 pr-4 py-2.5 text-xs sm:text-sm rounded-xl border border-slate-200 focus:ring-2 focus:ring-red-500/20 focus:border-red-500 outline-none transition bg-white text-slate-800 font-medium">"""

new_conf = """<input type="password" id="id_reg_confirm_password" name="confirm_password" required placeholder="{{ t.placeholder_confirm_password|default:'Confirm your password' }}"
                                       class="w-full pl-10 pr-10 py-2.5 text-xs sm:text-sm rounded-xl border border-slate-200 focus:ring-2 focus:ring-red-500/20 focus:border-red-500 outline-none transition bg-white text-slate-800 font-medium">
                                <button type="button" 
                                        onclick="const inp = document.getElementById('id_reg_confirm_password'); const icon = this.querySelector('i'); if (inp.type === 'password') { inp.type = 'text'; icon.classList.remove('fa-eye'); icon.classList.add('fa-eye-slash'); } else { inp.type = 'password'; icon.classList.remove('fa-eye-slash'); icon.classList.add('fa-eye'); }"
                                        class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-600 focus:outline-none transition cursor-pointer" 
                                        title="Show / Hide Password">
                                    <i class="fa-solid fa-eye text-sm"></i>
                                </button>"""

c_norm = c.replace('\r\n', '\n')
old_pass_norm = old_pass.replace('\r\n', '\n')
old_conf_norm = old_conf.replace('\r\n', '\n')

print('Pass found:', old_pass_norm in c_norm)
print('Conf found:', old_conf_norm in c_norm)

c_norm = c_norm.replace(old_pass_norm, new_pass)
c_norm = c_norm.replace(old_conf_norm, new_conf)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c_norm)
print('Updated register.html!')

