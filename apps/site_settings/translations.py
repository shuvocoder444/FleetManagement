"""
Bilingual Dictionary (English & Russian) for Topd Platform.
Works directly on Windows/Linux without requiring external GNU gettext/msgfmt binaries.
"""

TRANSLATIONS = {
    'en': {
        # Nav
        'home': 'Home',
        'about': 'About',
        'features': 'Features',
        'pricing': 'Pricing',
        'contact': 'Contact',
        'dashboard': 'Dashboard',
        'check_driver': 'Check Driver',
        'get_started': 'Get Started',
        'check_data': 'Check Data',
        'sign_in': 'Sign In',
        'logout': 'Logout',
        'profile': 'Profile',
        'settings': 'Settings',

        # Hero
        'hero_title': "Kyrgyzstan's First Unified Vehicle Rental Platform",
        'hero_subtitle': "Streamline your vehicle rental, leasing, and installment operations with our comprehensive platform. Connect with customers, manage contracts, and grow your business efficiently.",

        # How It Works
        'how_it_works': 'How It Works',
        'how_it_works_sub': 'Simple and efficient process to get you started in minutes',
        'step_1_title': 'Register',
        'step_1_desc': 'Create your account and complete your business profile to get started',
        'step_2_title': 'Create Contract',
        'step_2_desc': 'Generate and customize rental, leasing, or installment contracts',
        'step_3_title': 'Track & Earn',
        'step_3_desc': 'Monitor your operations and track your earnings in real-time',

        # Who It's For
        'who_its_for': "Who It's For",
        'who_its_for_sub': 'Our platform serves various stakeholders in the vehicle industry',
        'target_1_title': 'Rental Companies',
        'target_1_desc': 'Manage your fleet, bookings, and customer relationships effortlessly',
        'target_2_title': 'Leasing Providers',
        'target_2_desc': 'Streamline your leasing processes and payment tracking',
        'target_3_title': 'Private Owner',
        'target_3_desc': 'Find the best vehicle rental and leasing options to fit your needs',

        # Key Benefits
        'key_benefits': 'Key Benefits',
        'key_benefits_sub': 'Why choose Topd for your vehicle management needs',
        'benefit_1_title': 'Driver Ratings',
        'benefit_1_desc': 'Track driver performance and reliability',
        'benefit_2_title': 'Daily Payment Logs',
        'benefit_2_desc': 'Automated payment tracking and reporting',
        'benefit_3_title': 'Streamlined Contracts',
        'benefit_3_desc': 'Manage all contracts in one place',
        'benefit_4_title': 'Analytics Dashboard',
        'benefit_4_desc': 'Real-time insights and performance metrics',
        'benefit_5_title': 'Mobile Friendly',
        'benefit_5_desc': 'Manage on the go with our responsive platform',
        'benefit_6_title': 'Secure Platform',
        'benefit_6_desc': 'Bank-level security for your data',

        # Pricing
        'pricing_title': 'Our Pricing Models',
        'pricing_sub': 'Choose the model that works best for your business needs',
        'plan_1_name': 'Pay-per-Check',
        'plan_1_sub': 'Perfect for occasional users',
        'plan_1_price': '$2',
        'plan_1_unit': '/ check',
        'plan_1_f1': 'Single access to driver records',
        'plan_1_f2': 'No monthly commitment',
        'plan_1_f3': 'Perfect for one-time checks',
        'plan_1_f4': 'Quick and easy verification',
        'plan_1_btn': 'Pay-per-Check',

        'plan_2_name': 'Premium Subscription',
        'plan_2_sub': 'Complete solution for established businesses',
        'plan_2_badge': 'BEST VALUE',
        'plan_2_price': '$10',
        'plan_2_unit': '/ month',
        'plan_2_f1': 'Access to driver rating reviews',
        'plan_2_f2': 'Contract tracking dashboard',
        'plan_2_f3': 'Create and manage contracts',
        'plan_2_f4': 'Advanced reporting tools',
        'plan_2_f5': 'Priority customer support',
        'plan_2_btn': 'Choose Member',

        # CTA
        'cta_title': 'Ready to Transform Your Vehicle Business?',
        'cta_sub': 'Join thousands of businesses and individuals using Topd to streamline their operations',
        'learn_more': 'Learn More',

        # Contact
        'contact_us': 'Contact Us',
        'contact_sub': 'Have questions or need assistance? Get in touch with our team.',
        'get_in_touch': 'Get In Touch',
        'address_label': 'Address',
        'phone_label': 'Phone',
        'email_label': 'Email',
        'hours_label': 'Working Hours',
        'full_name_label': 'Full Name *',
        'email_address_label': 'Email Address *',
        'phone_number_label': 'Phone Number',
        'message_label': 'Message *',
        'send_message': 'Send Message',

        # Dashboard General
        'welcome_back': 'Welcome back',
        'dashboard_sub': "Here's what's happening with your vehicle rental business today.",
        'create_agreement': 'Create Agreement',
        'subscriber_metrics': 'Subscriber Metrics',
        'total_subscribers': 'Total Subscribers',
        'active_subscribers': 'Active Subscribers',
        'pending_approval': 'Pending Approval',
        'one_time_orders': 'One time Orders',
        'total_contracts': 'Total Contracts',
        'active_contracts': 'Active Contracts',
        'payments_received': 'Payments Received',
        
        # Statuses
        'vehicle_status': 'Vehicle Status',
        'available': 'Available',
        'rented': 'Rented',
        'leased': 'Leased',
        'maintenance': 'Maintenance',

        'driver_status': 'Driver Status',
        'total': 'Total',
        'busy': 'Busy',
        'bad': 'Bad / Warning',

        # Driver Check Form
        'check_driver_heading': 'Check a driver',
        'check_driver_sub': 'To check a driver background and incident history, input passport number or 14-digit personal ID number.',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'passport_number': 'Passport Number',
        'personal_id': 'Personal ID Number',
        'search_driver': 'Search Driver',
        'clear': 'Clear',

        # Driver Portal
        'driver_portal': 'Driver Portal',
        'driver_profile_title': 'Driver Profile & Performance',
        'total_agreements': 'Total Agreements',
        'completed': 'Completed',
        'problems': 'Problems',
        'total_issues': 'Total Issues',
        'completion_rate': 'Completion Rate',
        'total_reviews': 'Total Reviews',
        'current_assigned_vehicle': 'Current Assigned Vehicle',
        'incident_history_log': 'Incident & History Log',
        'admin_comments': 'Admin Comments',
        'license_expiry': 'License Expiry',
        'passport_expiry': 'Passport Expiry',
    },
    'ru': {
        # Nav
        'home': 'Главная',
        'about': 'О нас',
        'features': 'Возможности',
        'pricing': 'Тарифы',
        'contact': 'Контакты',
        'dashboard': 'Панель управления',
        'check_driver': 'Проверить водителя',
        'get_started': 'Начать работу',
        'check_data': 'Проверить данные',
        'sign_in': 'Войти',
        'logout': 'Выйти',
        'profile': 'Профиль',
        'settings': 'Настройки',

        # Hero
        'hero_title': 'Первая единая платформа аренды автомобилей в Кыргызстане',
        'hero_subtitle': 'Оптимизируйте операции аренды, лизинга и выкупа автомобилей с помощью нашей комплексной платформы. Находите клиентов, управляйте договорами и развивайте бизнес эффективно.',

        # How It Works
        'how_it_works': 'Как это работает',
        'how_it_works_sub': 'Простой и эффективный процесс начала работы за пару минут',
        'step_1_title': 'Регистрация',
        'step_1_desc': 'Создайте аккаунт и заполните профиль вашей компании для старта',
        'step_2_title': 'Создание договора',
        'step_2_desc': 'Создавайте и настраивайте договоры аренды, лизинга или выкупа авто',
        'step_3_title': 'Контроль и доход',
        'step_3_desc': 'Отслеживайте работу автопарка и контролируйте доходы в реальном времени',

        # Who It's For
        'who_its_for': 'Для кого это создано',
        'who_its_for_sub': 'Наша платформа объединяет ключевых участников авторынка',
        'target_1_title': 'Автопрокатные компании',
        'target_1_desc': 'Легко управляйте автопарком, бронированиями и клиентами в единой системе',
        'target_2_title': 'Лизинговые компании',
        'target_2_desc': 'Упрощайте процессы лизинга и контроль регулярных платежей',
        'target_3_title': 'Частные автовладельцы',
        'target_3_desc': 'Сдавайте личный автомобиль в аренду надежным водителям безопасно',

        # Key Benefits
        'key_benefits': 'Ключевые преимущества',
        'key_benefits_sub': 'Почему для управления автопарком выбирают Topd',
        'benefit_1_title': 'Рейтинг водителей',
        'benefit_1_desc': 'Отслеживайте надежность, штрафы и репутацию водителей',
        'benefit_2_title': 'Учет ежедневных платежей',
        'benefit_2_desc': 'Автоматический учет поступивших оплат и задолженностей',
        'benefit_3_title': 'Удобные договоры',
        'benefit_3_desc': 'Все договоры аренды, акты и фото осмотра в одном месте',
        'benefit_4_title': 'Аналитическая панель',
        'benefit_4_desc': 'Актуальная аналитика и показатели эффективности в реальном времени',
        'benefit_5_title': 'Мобильная адаптивность',
        'benefit_5_desc': 'Удобно управляйте бизнесом прямо со смартфона или планшета',
        'benefit_6_title': 'Надежная платформа',
        'benefit_6_desc': 'Безопасность банковского уровня для защиты ваших данных',

        # Pricing
        'pricing_title': 'Наши тарифные планы',
        'pricing_sub': 'Выберите тариф, который идеально подходит для вашего бизнеса',
        'plan_1_name': 'Оплата за проверку',
        'plan_1_sub': 'Идеально для разовых проверок водителей',
        'plan_1_price': '$2',
        'plan_1_unit': '/ за проверку',
        'plan_1_f1': 'Разовый доступ к истории и штрафам водителя',
        'plan_1_f2': 'Без ежемесячной абонентской платы',
        'plan_1_f3': 'Идеально для индивидуальных автовладельцев',
        'plan_1_f4': 'Быстрая и точная верификация',
        'plan_1_btn': 'Оплатить проверку',

        'plan_2_name': 'Премиум подписка',
        'plan_2_sub': 'Полное решение для автопрокатных компаний',
        'plan_2_badge': 'ВЫГОДНЫЙ ВЫБОР',
        'plan_2_price': '$10',
        'plan_2_unit': '/ в месяц',
        'plan_2_f1': 'Полный доступ к базе отзывов и черному списку',
        'plan_2_f2': 'Панель отслеживания всех договоров и авто',
        'plan_2_f3': 'Создание и учет договоров аренды',
        'plan_2_f4': 'Расширенные отчеты и аналитика',
        'plan_2_f5': 'Приоритетная служба поддержки 24/7',
        'plan_2_btn': 'Выбрать тариф',

        # CTA
        'cta_title': 'Готовы масштабировать свой автопрокатный бизнес?',
        'cta_sub': 'Присоединяйтесь к тысячам компаний и автовладельцев, использующих Topd',
        'learn_more': 'Узнать больше',

        # Contact
        'contact_us': 'Свяжитесь с нами',
        'contact_sub': 'Есть вопросы или нужна консультация? Наша команда всегда на связи.',
        'get_in_touch': 'Контакты',
        'address_label': 'Адрес',
        'phone_label': 'Телефон',
        'email_label': 'Эл. почта',
        'hours_label': 'Режим работы',
        'full_name_label': 'ФИО *',
        'email_address_label': 'Адрес электронной почты *',
        'phone_number_label': 'Номер телефона',
        'message_label': 'Сообщение *',
        'send_message': 'Отправить сообщение',

        # Dashboard General
        'welcome_back': 'С возвращением',
        'dashboard_sub': 'Вот сводка по вашему автопрокатному бизнесу на сегодня.',
        'create_agreement': 'Создать договор',
        'subscriber_metrics': 'Метрики подписчиков',
        'total_subscribers': 'Всего подписчиков',
        'active_subscribers': 'Активные подписчики',
        'pending_approval': 'Ожидает одобрения',
        'one_time_orders': 'Разовые заказы',
        'total_contracts': 'Всего договоров',
        'active_contracts': 'Активные договоры',
        'payments_received': 'Полученные платежи',
        
        # Statuses
        'vehicle_status': 'Статус автомобилей',
        'available': 'Доступно',
        'rented': 'В аренде',
        'leased': 'В лизинге',
        'maintenance': 'Техобслуживание',

        'driver_status': 'Статус водителей',
        'total': 'Всего',
        'busy': 'Занят',
        'bad': 'Проблемный / Предупреждение',

        # Driver Check Form
        'check_driver_heading': 'Проверить водителя',
        'check_driver_sub': 'Для проверки репутации и штрафов водителя введите номер паспорта или 14-значный ПИН/ИНН.',
        'first_name': 'Имя',
        'last_name': 'Фамилия',
        'passport_number': 'Номер паспорта',
        'personal_id': 'Персональный номер (ИНН)',
        'search_driver': 'Найти водителя',
        'clear': 'Очистить',

        # Driver Portal
        'driver_portal': 'Портал водителя',
        'driver_profile_title': 'Профиль и показатели водителя',
        'total_agreements': 'Всего договоров',
        'completed': 'Завершено',
        'problems': 'Проблемы',
        'total_issues': 'Всего инцидентов',
        'completion_rate': 'Процент успешности',
        'total_reviews': 'Всего отзывов',
        'current_assigned_vehicle': 'Текущий закрепленный автомобиль',
        'incident_history_log': 'История инцидентов и штрафов',
        'admin_comments': 'Комментарии администрации',
        'license_expiry': 'Срок водительского удостоверения',
        'passport_expiry': 'Срок действия паспорта',
    }
}


def get_translation(lang_code):
    """Returns translation dictionary for the selected language, defaulting to English."""
    if lang_code in TRANSLATIONS:
        return TRANSLATIONS[lang_code]
    return TRANSLATIONS['en']
