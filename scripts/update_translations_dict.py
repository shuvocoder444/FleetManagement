# Script to update translations.py with complete frontend translations for EN and RU
import os, sys

translations_file = r'D:\new\apps\site_settings\translations.py'

NEW_EN = {
    # Brand, Global & Footer
    'quick_links': 'Quick Links',
    'legal_privacy': 'Legal & Privacy',
    'contact_info': 'Contact Info',
    'all_rights_reserved': 'All rights reserved.',
    'footer_desc': "Kyrgyzstan's premier digital platform for vehicle rentals, fleet management, and anti-fraud driver background checks.",
    'headquarters': 'Headquarters',
    'office_address': 'Office Address',
    'email_support': 'Email Support',
    'phone_support': 'Phone Support',
    'working_hours_label': 'Working Hours',
    'working_hours_val': 'Mon - Fri: 9:00 AM - 6:00 PM',
    'buy_subscription': 'Buy Subscription',
    'register_btn': 'Register',

    # Home Page
    'stat_agreements': 'Agreements Created',
    'stat_drivers': 'Verified Drivers',
    'stat_vehicles': 'Fleet Vehicles',
    'stat_fraud': 'Fraud Prevention',
    'read_full_story': 'Read our full company story & roadmap',
    'features_benefits_badge': 'Features & Benefits',
    'why_choose_title': 'Why Choose Our Platform',
    'why_choose_sub': 'Comprehensive fleet software designed specifically for the Central Asian car rental market.',
    'feature_anti_fraud_title': 'Anti-Fraud Driver Check',
    'feature_anti_fraud_desc': 'Search driver history by passport or PIN to instantly uncover unpaid fines, disappeared cars, or contract violations before handing over keys.',
    'feature_wizard_title': '3-Step Agreement Wizard',
    'feature_wizard_desc': 'Quickly generate short-term, long-term, leasing, and installment contracts complete with photo inspection records.',
    'feature_garage_title': 'Fleet & Garage Management',
    'feature_garage_desc': 'Organize your vehicles by status (Available, Rented, Leased, Maintenance), upload documents and track maintenance.',
    'explore_all_features': 'Explore All Features & Capabilities',
    'view_pricing_faq': 'View Full Pricing Comparison & FAQ',
    'cta_ready_title': 'Ready to Protect Your Fleet and Accelerate Growth?',
    'cta_ready_sub': 'Join hundreds of vehicle rental companies across Kyrgyzstan utilizing our digital contracts and driver verification engine.',
    'get_started_now': 'Get Started Now',
    'contact_sales': 'Contact Sales',

    # About Us Page
    'about_badge': 'Our Mission & Platform',
    'about_title': 'About Us',
    'about_subtitle': 'Building the most reliable, unified digital fleet ecosystem and driver anti-fraud network for Kyrgyzstan and Central Asia.',
    'who_we_are': 'Who We Are',
    'about_empower_title': 'Empowering Car Rental Companies With Technology & Trust',
    'about_p1': 'Vehicle rental operations have traditionally suffered from paper-heavy agreements, untracked vehicle handovers, and high risks of fraud, unpaid fines, or vehicle disappearance.',
    'about_p2': 'Topd was engineered from the ground up to eliminate these risks. We provide a single cloud platform where fleet owners, rental companies, and leasing operators can verify drivers against unified blacklist data, generate legally enforceable contracts with pre-rental condition photos, and automate payments.',
    'risk_reduction': 'Risk Reduction',
    'agreement_gen_speed': '3-Minute Agreement Generation',
    'core_pillars_title': 'Our Core Pillars',
    'core_pillars_sub': 'How Topd delivers peace of mind to every rental business owner',
    'pillar_1_title': 'Anti-Fraud Protection',
    'pillar_1_desc': 'A centralized, crowd-verified record of driver incidents across all participating agencies. Never unknowingly hand over expensive vehicles to repeat offenders.',
    'pillar_2_title': 'Digital Paperwork',
    'pillar_2_desc': 'Say goodbye to misplaced paperwork. Digital agreements with photo inspection, damage checklists, and clear payment terms keep your business protected.',
    'pillar_3_title': 'Localized Billing',
    'pillar_3_desc': 'Designed for Central Asia: multiple currencies (KGS Som, USD), manual bank transfers, cash tracking, and flexible pay-per-check billing models.',
    'about_cta_title': 'Ready to upgrade your car rental business?',
    'about_cta_sub': 'Get started today with our flexible subscription plans or test our driver check tool.',
    'view_pricing_plans': 'View Pricing Plans',
    'contact_our_team': 'Contact Our Team',

    # Features Page
    'features_badge': 'All-In-One SaaS Suite',
    'features_title': 'Platform Features',
    'features_subtitle': 'Discover all the built-in tools that make Topd the leading fleet and anti-fraud verification engine in Kyrgyzstan.',
    'feat_anti_fraud_badge': 'Anti-Fraud Verification',
    'feat_anti_fraud_h2': 'Check Driver Background Before Handing Over Keys',
    'feat_anti_fraud_lead': 'Protect your expensive vehicles against dishonest renters. Our unified Anti-Fraud Verification Engine queries a shared regional database of driver histories.',
    'feat_search_pin_title': 'Search by Passport or PIN',
    'feat_search_pin_desc': 'Query using passport numbers or official 14-digit national identification numbers.',
    'feat_7_incidents_title': '7 Critical Incident Classifications',
    'feat_7_incidents_desc': 'Flags non-payment, vehicle disappearance, unpaid police fines, contract violations, accidents, and suspicious fraud behavior.',
    'feat_reputation_title': '5-Star Agency Reputation Rating',
    'feat_reputation_desc': 'Check aggregate community ratings and private internal agency comments.',
    'try_driver_tool': 'Try Driver Check Tool',
    'feat_verified_badge': 'VERIFIED',
    'safety_score': 'Safety Score',
    'fraud_incidents': 'Fraud Incidents',
    'clean_record_msg': 'Clean Record — Driver is approved for all vehicle classes.',
    'feat_contracts_badge': 'Digital Contracts',
    'feat_wizard_h2': 'Issue Legal Rental Agreements in Under 3 Minutes',
    'feat_wizard_lead': 'Generate legally sound, customized contracts for any rental scenario without relying on cumbersome paper folders.',
    'feat_modalities_title': '5 Supported Contract Modalities',
    'feat_modalities_desc': 'Short-Term Rental, Long-Term Rental, Leasing, Installment, and Vehicle Buyout.',
    'feat_inspection_title': 'Pre-Rental Inspection Photos',
    'feat_inspection_desc': 'Record vehicle body condition, scratches, fuel levels, and odometer before handover.',
    'feat_fleet_badge': 'Complete Fleet Control',
    'feat_unified_h2': 'Unified Ecosystem for Every Team Member',
    'feat_unified_lead': 'Topd provides tailored dashboard interfaces for Super Administrators, Rental Companies, and Drivers.',
    'superadmin_portal_title': 'Super Admin Master Portal',
    'superadmin_portal_desc': 'Full visibility over all subscribers, manual bank payment approvals, user management, and platform-wide website configuration.',
    'company_portal_title': 'Rental Company Portal',
    'company_portal_desc': 'Complete garage fleet management (Available, Rented, Maintenance), agreement creator, driver assignment, and live subscription status.',
    'driver_portal_title': 'Driver Portal',
    'driver_portal_desc': 'Drivers can view their active assigned vehicle, review signed contracts, check personal performance ratings, and view incident history.',
    'features_cta_title': 'Empower your operations with Topd today',
    'features_cta_sub': 'Choose a plan that fits your business or speak with our Bishkek operations team.',

    # Pricing Page
    'pricing_badge': 'Transparent Pricing',
    'pricing_page_title': 'Plans & Subscriptions',
    'pricing_page_sub': 'Choose the right plan for your fleet size with full support for bank transfer, cash, and mobile money.',
    'perk_anti_fraud': 'Anti-Fraud Driver Check Tool',
    'perk_wizard': '3-Step Digital Agreement Wizard',
    'perk_garage': 'Fleet Garage Management',
    'perk_payments': 'Manual Payment & Bank Slip Approval',
    'payment_options_title': 'Flexible Payment Options Supported',
    'payment_options_sub': 'Easy activation through local banking channels in Kyrgyzstan and international wire',
    'demir_title': 'Demir Bank (DKIB)',
    'demir_desc': 'Direct wire transfer in USD or KGS Som to our corporate account.',
    'mobile_bank_title': 'Mobile Banking',
    'mobile_bank_desc': 'Instant transfer via mBank, Elsom, or regional mobile money.',
    'cash_title': 'Cash Deposit',
    'cash_desc': 'Hand delivery or cash deposit at our Bishkek office with official receipt.',
    'faq_badge': 'Got Questions?',
    'faq_title': 'Frequently Asked Questions',
    'faq_sub': 'Everything you need to know about purchasing and managing your Topd subscription.',
    'faq_1_q': 'How does subscription purchasing work?',
    'faq_1_a': 'Simply choose your preferred plan on this page, click "Buy Subscription", and you will see our bank transfer and mobile wallet instructions. Complete the transfer through your banking app and submit the transaction reference code. Our operations team verifies and activates your subscription within 15–30 minutes.',
    'faq_2_q': 'Can I pay in Kyrgyzstani Som (KGS) or USD?',
    'faq_2_a': 'Yes! Both currencies are fully supported. You can pay via Demir Bank in USD or converted KGS Som using the official daily rate.',
    'faq_3_q': 'What is the "Pay Per Check" plan?',
    'faq_3_a': 'The Pay Per Check plan is tailored for occasional rental agencies or individual owners who only need to verify a driver once or twice. Each check costs only $2.00 without requiring a monthly commitment.',
    'faq_4_q': 'How do I track my active subscriptions and payment history?',
    'faq_4_a': 'Once logged in, open the "My Subscription" page from your dashboard or profile dropdown. You will see live expiration dates, payment receipts, and approval statuses.',

    # Contact Page
    'contact_badge': 'Get In Touch',
    'contact_page_title': 'Contact Us',
    'contact_page_sub': 'Have questions about fleet integration, driver verification, or custom enterprise plans? Our Bishkek team is here to help.',
    'send_message_badge': 'Send a Message',
    'contact_form_title': "We'd Love to Hear From You",
    'contact_form_sub': 'Fill out the form below and we will respond within 24 business hours.',
    'label_full_name': 'Full Name',
    'label_email_address': 'Email Address',
    'label_phone_number': 'Phone Number',
    'label_your_message': 'Your Message',
    'placeholder_name': 'e.g. Azamat Isakov',
    'placeholder_email': 'azamat@company.kg',
    'placeholder_phone': '+996 555 123 456',
    'placeholder_message': 'Tell us how we can help your car rental company or fleet operations...',
    'btn_send_message': 'Send Message',
    'contact_info_box': 'Contact Information',

    # Terms & Privacy
    'terms_badge': 'Legal & Compliance',
    'terms_title': 'Terms & Conditions',
    'terms_subtitle': 'Last updated: October 2026. Please read these terms carefully before utilizing the Topd platform.',
    'privacy_badge': 'Privacy & Data Protection',
    'privacy_title': 'Privacy Policy',
    'privacy_subtitle': 'Last updated: October 2026. How Topd collects, safeguards, and handles vehicle and driver verification data in the Kyrgyz Republic.',
}

NEW_RU = {
    # Brand, Global & Footer
    'quick_links': 'Быстрые ссылки',
    'legal_privacy': 'Правовая информация',
    'contact_info': 'Контакты',
    'all_rights_reserved': 'Все права защищены.',
    'footer_desc': 'Ведущая цифровая платформа Кыргызстана по аренде, лизингу, управлению автопарком и проверке водителей.',
    'headquarters': 'Главный офис',
    'office_address': 'Адрес офиса',
    'email_support': 'Электронная почта',
    'phone_support': 'Телефон поддержки',
    'working_hours_label': 'Режим работы',
    'working_hours_val': 'Пн - Пт: 9:00 - 18:00',
    'buy_subscription': 'Купить подписку',
    'register_btn': 'Регистрация',

    # Home Page
    'stat_agreements': 'Создано договоров',
    'stat_drivers': 'Проверенных водителей',
    'stat_vehicles': 'Автомобилей в парке',
    'stat_fraud': 'Защита от мошенничества',
    'read_full_story': 'Узнать больше о нашей компании и развитии',
    'features_benefits_badge': 'Возможности и преимущества',
    'why_choose_title': 'Почему выбирают нашу платформу',
    'why_choose_sub': 'Специализированное ПО для автопроката, адаптированное под рынок Центральной Азии.',
    'feature_anti_fraud_title': 'Проверка водителей на мошенничество',
    'feature_anti_fraud_desc': 'Поиск по паспорту или ИНН для моментального выявления неоплаченных штрафов, угонов и нарушений условий аренды до передачи ключей.',
    'feature_wizard_title': 'Быстрое оформление договора в 3 шага',
    'feature_wizard_desc': 'Моментальное составление краткосрочных, долгосрочных, лизинговых договоров и договоров выкупа с фотофиксацией состояния авто.',
    'feature_garage_title': 'Управление автопарком и гаражом',
    'feature_garage_desc': 'Удобный учет авто по статусам (Свободен, В аренде, В лизинге, На ТО), хранение документов и контроль обслуживания.',
    'explore_all_features': 'Все возможности платформы',
    'view_pricing_faq': 'Сравнение тарифов и ответы на вопросы',
    'cta_ready_title': 'Готовы защитить свой автопарк и ускорить рост бизнеса?',
    'cta_ready_sub': 'Присоединяйтесь к сотням автопрокатных компаний Кыргызстана, использующих наши цифровые договоры и проверку водителей.',
    'get_started_now': 'Начать прямо сейчас',
    'contact_sales': 'Связаться с нами',

    # About Us Page
    'about_badge': 'Наша миссия и платформа',
    'about_title': 'О нас',
    'about_subtitle': 'Создание надежной единой цифровой экосистемы автопарков и сети защиты от мошенничества в Кыргызстане и Центральной Азии.',
    'who_we_are': 'Кто мы',
    'about_empower_title': 'Усиливаем автопрокатный бизнес технологиями и доверием',
    'about_p1': 'Традиционный автопрокат страдает от бумажной волокиты, неконтролируемой передачи автомобилей и высоких рисков мошенничества, неоплаченных штрафов или угонов.',
    'about_p2': 'Topd был разработан с нуля для полного устранения этих рисков. Мы предоставляем единую облачную платформу, где владельцы автопарков могут проверять водителей по единой базе нарушений, формировать юридически грамотные электронные договоры с фотофиксацией и автоматизировать платежи.',
    'risk_reduction': 'Снижение рисков',
    'agreement_gen_speed': 'Оформление договора за 3 минуты',
    'core_pillars_title': 'Наши ключевые принципы',
    'core_pillars_sub': 'Как Topd обеспечивает уверенность и безопасность каждому владельцу автобизнеса',
    'pillar_1_title': 'Защита от мошенничества',
    'pillar_1_desc': 'Централизованная база инцидентов от всех автопрокатов. Вы никогда не отдадите автомобиль недобросовестному водителю или мошеннику.',
    'pillar_2_title': 'Цифровой документооборот',
    'pillar_2_desc': 'Забудьте о потерянных бумажных актах. Электронные договоры с фотоосмотром, картой повреждений и четкими условиями защищают ваш бизнес.',
    'pillar_3_title': 'Адаптированные платежи',
    'pillar_3_desc': 'Создано для Центральной Азии: поддержка сомов (KGS) и долларов (USD), банковские переводы, учет наличных и оплата за разовые проверки.',
    'about_cta_title': 'Готовы вывести свой автопрокат на новый уровень?',
    'about_cta_sub': 'Начните сегодня с нашими гибкими тарифами или протестируйте сервис проверки водителей.',
    'view_pricing_plans': 'Посмотреть тарифы',
    'contact_our_team': 'Связаться с командой',

    # Features Page
    'features_badge': 'Единая SaaS-платформа',
    'features_title': 'Возможности платформы',
    'features_subtitle': 'Узнайте о всех инструментах, делающих Topd ведущей платформой управления автопарком и проверки водителей в Кыргызстане.',
    'feat_anti_fraud_badge': 'Проверка на мошенничество',
    'feat_anti_fraud_h2': 'Проверяйте историю водителя до передачи ключей',
    'feat_anti_fraud_lead': 'Защитите свои дорогие автомобили от недобросовестных арендаторов. Единая система проверки запрашивает региональную базу историй водителей.',
    'feat_search_pin_title': 'Поиск по паспорту или ИНН',
    'feat_search_pin_desc': 'Быстрый поиск по серии и номеру паспорта или 14-значному персональному ИНН.',
    'feat_7_incidents_title': '7 категорий нарушений',
    'feat_7_incidents_desc': 'Фиксация невыплат, угонов, неоплаченных штрафов, нарушений договора, ДТП и подозрительного поведения.',
    'feat_reputation_title': '5-звездочный рейтинг репутации',
    'feat_reputation_desc': 'Общий рейтинг сообщества и закрытые отзывы компаний-партнеров.',
    'try_driver_tool': 'Проверить водителя прямо сейчас',
    'feat_verified_badge': 'ПРОВЕРЕН',
    'safety_score': 'Рейтинг безопасности',
    'fraud_incidents': 'Нарушения',
    'clean_record_msg': 'Чистая история — водитель допущен к аренде всех классов авто.',
    'feat_contracts_badge': 'Электронные договоры',
    'feat_wizard_h2': 'Оформляйте официальные договоры аренды за 3 минуты',
    'feat_wizard_lead': 'Создавайте юридически безупречные электронные договоры для любых видов аренды без бумажной рутины.',
    'feat_modalities_title': '5 видов договоров',
    'feat_modalities_desc': 'Посуточная аренда, долгосрочная аренда, лизинг, рассрочка и выкуп автомобиля.',
    'feat_inspection_title': 'Фотофиксация до аренды',
    'feat_inspection_desc': 'Фиксация состояния кузова, царапин, уровня топлива и пробега до передачи авто.',
    'feat_fleet_badge': 'Полный контроль автопарка',
    'feat_unified_h2': 'Единая экосистема для всех участников',
    'feat_unified_lead': 'Topd предоставляет отдельные кабинеты для Главного администратора, Компаний автопроката и Водителей.',
    'superadmin_portal_title': 'Кабинет Главного Администратора',
    'superadmin_portal_desc': 'Полный контроль над подписчиками, одобрение банковских платежей, управление пользователями и общие настройки системы.',
    'company_portal_title': 'Кабинет Автопрокатной Компании',
    'company_portal_desc': 'Управление гаражом (Свободен, В аренде, На ТО), создание договоров, назначение водителей и статус подписки.',
    'driver_portal_title': 'Кабинет Водителя',
    'driver_portal_desc': 'Водители могут видеть закрепленный автомобиль, просматривать подписанные договоры, свой рейтинг и историю поездок.',
    'features_cta_title': 'Автоматизируйте работу автопарка с Topd уже сегодня',
    'features_cta_sub': 'Выберите подходящий тариф или свяжитесь с нашим офисом в Бишкеке.',

    # Pricing Page
    'pricing_badge': 'Прозрачные тарифы',
    'pricing_page_title': 'Тарифы и подписка',
    'pricing_page_sub': 'Выберите идеальный тариф для вашего автопарка с поддержкой банковского перевода, наличных и мобильных кошельков.',
    'perk_anti_fraud': 'Сервис проверки водителей на мошенничество',
    'perk_wizard': 'Мастер оформления договоров в 3 шага',
    'perk_garage': 'Управление гаражом и парком авто',
    'perk_payments': 'Оплата банковским переводом и квитанцией',
    'payment_options_title': 'Удобные способы оплаты',
    'payment_options_sub': 'Простая активация через банки Кыргызстана и международные переводы',
    'demir_title': 'Демир Банк (DKIB)',
    'demir_desc': 'Прямой безналичный расчет в сомах (KGS) или долларах (USD) на наш расчетный счет.',
    'mobile_bank_title': 'Мобильные банки',
    'mobile_bank_desc': 'Моментальная оплата через mBank, Элсом или региональные кошельки.',
    'cash_title': 'Оплата наличными',
    'cash_desc': 'Оплата в нашем офисе в Бишкеке с выдачей официального чека и квитанции.',
    'faq_badge': 'Остались вопросы?',
    'faq_title': 'Часто задаваемые вопросы',
    'faq_sub': 'Все, что нужно знать об оплате и управлении подпиской Topd.',
    'faq_1_q': 'Как происходит оформление и оплата подписки?',
    'faq_1_a': 'Выберите подходящий тариф на этой странице, нажмите "Купить подписку" и ознакомьтесь с реквизитами для перевода. Совершите оплату через банковское приложение и укажите код транзакции. Наша служба активирует подписку в течение 15–30 минут.',
    'faq_2_q': 'Можно ли оплатить в сомах (KGS) или долларах (USD)?',
    'faq_2_a': 'Да! Поддерживаются обе валюты. Вы можете оплатить через Демир Банк в долларах США или в сомах по курсу на день оплаты.',
    'faq_3_q': 'Что такое тариф "Оплата за проверку"?',
    'faq_3_a': 'Тариф "Оплата за проверку" подходит частным владельцам и небольшим прокатам, которым проверка нужна периодически. Стоимость одной проверки — всего $2.00 без абонентской платы.',
    'faq_4_q': 'Как отслеживать статус подписки и историю оплат?',
    'faq_4_a': 'После входа в аккаунт перейдите в раздел "Моя подписка". Там отображаются срок действия, квитанции и статус одобрения.',

    # Contact Page
    'contact_badge': 'Свяжитесь с нами',
    'contact_page_title': 'Контакты',
    'contact_page_sub': 'Есть вопросы по подключению автопарка, проверке водителей или корпоративным тарифам? Наша команда в Бишкеке всегда готова помочь.',
    'send_message_badge': 'Отправить сообщение',
    'contact_form_title': 'Мы всегда на связи',
    'contact_form_sub': 'Заполните форму ниже, и мы ответим вам в течение рабочего дня.',
    'label_full_name': 'Ваше имя',
    'label_email_address': 'Электронная почта',
    'label_phone_number': 'Номер телефона',
    'label_your_message': 'Ваше сообщение',
    'placeholder_name': 'например, Азамат Исаков',
    'placeholder_email': 'azamat@company.kg',
    'placeholder_phone': '+996 555 123 456',
    'placeholder_message': 'Расскажите, как мы можем помочь вашему автопарку или компании...',
    'btn_send_message': 'Отправить сообщение',
    'contact_info_box': 'Контактная информация',

    # Terms & Privacy
    'terms_badge': 'Юридическая информация',
    'terms_title': 'Условия использования',
    'terms_subtitle': 'Последнее обновление: октябрь 2026 г. Пожалуйста, внимательно ознакомьтесь с условиями перед использованием платформы Topd.',
    'privacy_badge': 'Защита данных и конфиденциальность',
    'privacy_title': 'Политика конфиденциальности',
    'privacy_subtitle': 'Последнее обновление: октябрь 2026 г. Как платформа Topd собирает, хранит и защищает данные в Кыргызской Республике.',
}

with open(translations_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's import TRANSLATIONS and update it
sys.path.insert(0, r'D:\new')
from apps.site_settings.translations import TRANSLATIONS

for k, v in NEW_EN.items():
    TRANSLATIONS['en'][k] = v

for k, v in NEW_RU.items():
    TRANSLATIONS['ru'][k] = v

import pprint

output = f'''"""
Comprehensive Bilingual Dictionary (English & Russian) for Topd Platform.
100% Covers Landing Page, Header, Footer, Sidebar, Super Admin, Fleet Admin & Driver Dashboards.
"""

TRANSLATIONS = {pprint.pformat(TRANSLATIONS, indent=4, width=120, sort_dicts=False)}


def get_translation(lang_code):
    """
    Returns the translation dictionary for the given language code ('en' or 'ru').
    Defaults to 'en' if the language is unsupported.
    """
    if not lang_code or lang_code not in TRANSLATIONS:
        lang_code = 'en'
    return TRANSLATIONS[lang_code]
'''

with open(translations_file, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"SUCCESS: translations.py updated. EN keys: {len(TRANSLATIONS['en'])}, RU keys: {len(TRANSLATIONS['ru'])}")
