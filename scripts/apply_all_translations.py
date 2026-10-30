# Apply comprehensive bilingual translations to all frontend templates
import os

def update_index():
    path = r'D:\new\templates\landing\index.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Hero Title & Subtitle
    c = c.replace(
        '{{ page.title|default:t.hero_title|default:"Kyrgyzstan\'s First Unified Vehicle Rental Platform" }}',
        "{% if current_lang == 'ru' %}{{ t.hero_title }}{% else %}{{ page.title|default:t.hero_title }}{% endif %}"
    )
    c = c.replace(
        '{{ page.subtitle|default:t.hero_subtitle|default:"Streamline your vehicle rental, leasing, and installment operations with our comprehensive platform. Connect with customers, manage contracts, and grow your business efficiently." }}',
        "{% if current_lang == 'ru' %}{{ t.hero_subtitle }}{% else %}{{ page.subtitle|default:t.hero_subtitle }}{% endif %}"
    )

    # 2. Stats
    c = c.replace('Agreements Created', "{{ t.stat_agreements|default:'Agreements Created' }}")
    c = c.replace('Verified Drivers', "{{ t.stat_drivers|default:'Verified Drivers' }}")
    c = c.replace('Fleet Vehicles', "{{ t.stat_vehicles|default:'Fleet Vehicles' }}")
    c = c.replace('Fraud Prevention', "{{ t.stat_fraud|default:'Fraud Prevention' }}")

    # 3. How it works roadmap link
    c = c.replace('<span>Read our full company story & roadmap</span>', "<span>{{ t.read_full_story|default:'Read our full company story & roadmap' }}</span>")

    # 4. Features preview
    c = c.replace('Features & Benefits', "{{ t.features_benefits_badge|default:'Features & Benefits' }}")
    c = c.replace('Comprehensive fleet software designed specifically for the Central Asian car rental market.', "{{ t.why_choose_sub }}")
    c = c.replace('<h3 class="text-base font-bold text-slate-900 mb-2">Anti-Fraud Driver Check</h3>', '<h3 class="text-base font-bold text-slate-900 mb-2">{{ t.feature_anti_fraud_title }}</h3>')
    c = c.replace('Search driver history by passport or PIN to instantly uncover unpaid fines, disappeared cars, or contract violations before handing over keys.', '{{ t.feature_anti_fraud_desc }}')
    c = c.replace('<h3 class="text-base font-bold text-slate-900 mb-2">3-Step Agreement Wizard</h3>', '<h3 class="text-base font-bold text-slate-900 mb-2">{{ t.feature_wizard_title }}</h3>')
    c = c.replace('Quickly generate short-term, long-term, leasing, and installment contracts complete with photo inspection records.', '{{ t.feature_wizard_desc }}')
    c = c.replace('<h3 class="text-base font-bold text-slate-900 mb-2">Fleet & Garage Management</h3>', '<h3 class="text-base font-bold text-slate-900 mb-2">{{ t.feature_garage_title }}</h3>')
    c = c.replace('Organize your vehicles by status (Available, Rented, Leased, Maintenance), upload documents and track maintenance.', '{{ t.feature_garage_desc }}')
    c = c.replace('<span>Explore All Features & Capabilities</span>', '<span>{{ t.explore_all_features }}</span>')

    # 5. Pricing preview
    c = c.replace('Choose pay-per-check or unlimited monthly and yearly subscriptions with manual bank transfer support.', '{{ t.pricing_sub }}')
    c = c.replace('<span>View Full Pricing Comparison & FAQ</span>', '<span>{{ t.view_pricing_faq }}</span>')

    # 6. Bottom CTA
    c = c.replace('Ready to Protect Your Fleet and Accelerate Growth?', '{{ t.cta_ready_title }}')
    c = c.replace('Join hundreds of vehicle rental companies across Kyrgyzstan utilizing our digital contracts and driver verification engine.', '{{ t.cta_ready_sub }}')
    c = c.replace("{{ t.get_started|default:'Get Started Now' }}", '{{ t.get_started_now }}')
    c = c.replace("{{ t.contact|default:'Contact Sales' }}", '{{ t.contact_sales }}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("index.html updated successfully!")


def update_about():
    path = r'D:\new\templates\landing\about.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'Our Mission & Platform' }}", "{% if current_lang == 'ru' %}{{ t.about_badge }}{% else %}{{ page.badge|default:t.about_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:t.about|default:'About Us' }}", "{% if current_lang == 'ru' %}{{ t.about_title }}{% else %}{{ page.title|default:t.about }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:'Building the most reliable, unified digital fleet ecosystem and driver anti-fraud network for Kyrgyzstan and Central Asia.' }}", "{% if current_lang == 'ru' %}{{ t.about_subtitle }}{% else %}{{ page.subtitle|default:t.about_subtitle }}{% endif %}")

    # Who we are section
    c = c.replace('Who We Are', '{{ t.who_we_are|default:"Who We Are" }}')
    c = c.replace("{{ page.section_title|default:'Empowering Car Rental Companies With Technology & Trust' }}", "{% if current_lang == 'ru' %}{{ t.about_empower_title }}{% else %}{{ page.section_title|default:t.about_empower_title }}{% endif %}")

    c = c.replace(
        '<p>Vehicle rental operations have traditionally suffered from paper-heavy agreements, untracked vehicle handovers, and high risks of fraud, unpaid fines, or vehicle disappearance.</p>',
        '<p>{{ t.about_p1 }}</p>'
    )
    c = c.replace(
        "<p><strong>{{ site_setting.site_name|default:'Topd' }}</strong> was engineered from the ground up to eliminate these risks. We provide a single cloud platform where fleet owners, rental companies, and leasing operators can verify drivers against unified blacklist data, generate legally enforceable contracts with pre-rental condition photos, and automate payments.</p>",
        "<p><strong>{{ site_setting.site_name|default:'Topd' }}</strong> {{ t.about_p2 }}</p>"
    )

    c = c.replace('Risk Reduction', '{{ t.risk_reduction }}')
    c = c.replace('3-Minute', "3-{{ t.minute|default:'Min' }}")
    c = c.replace('Agreement Generation', '{{ t.agreement_gen_speed }}')
    c = c.replace('<p class="text-xs font-bold text-red-400 uppercase tracking-wider">Headquarters</p>', '<p class="text-xs font-bold text-red-400 uppercase tracking-wider">{{ t.headquarters }}</p>')

    # 3 core pillars
    c = c.replace('Our Core Pillars', '{{ t.core_pillars_title }}')
    c = c.replace('How Topd delivers peace of mind to every rental business owner', '{{ t.core_pillars_sub }}')
    c = c.replace('<h3 class="text-lg font-bold text-slate-900">Anti-Fraud Protection</h3>', '<h3 class="text-lg font-bold text-slate-900">{{ t.pillar_1_title }}</h3>')
    c = c.replace('A centralized, crowd-verified record of driver incidents across all participating agencies. Never unknowingly hand over expensive vehicles to repeat offenders.', '{{ t.pillar_1_desc }}')
    c = c.replace('<h3 class="text-lg font-bold text-slate-900">Digital Paperwork</h3>', '<h3 class="text-lg font-bold text-slate-900">{{ t.pillar_2_title }}</h3>')
    c = c.replace('Say goodbye to misplaced paperwork. Digital agreements with photo inspection, damage checklists, and clear payment terms keep your business protected.', '{{ t.pillar_2_desc }}')
    c = c.replace('<h3 class="text-lg font-bold text-slate-900">Localized Billing</h3>', '<h3 class="text-lg font-bold text-slate-900">{{ t.pillar_3_title }}</h3>')
    c = c.replace('Designed for Central Asia: multiple currencies (KGS Som, USD), manual bank transfers, cash tracking, and flexible pay-per-check billing models.', '{{ t.pillar_3_desc }}')

    # CTA Banner
    c = c.replace('Ready to upgrade your car rental business?', '{{ t.about_cta_title }}')
    c = c.replace('Get started today with our flexible subscription plans or test our driver check tool.', '{{ t.about_cta_sub }}')
    c = c.replace('View Pricing Plans', '{{ t.view_pricing_plans }}')
    c = c.replace('Contact Our Team', '{{ t.contact_our_team }}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("about.html updated successfully!")


def update_features():
    path = r'D:\new\templates\landing\features.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'All-In-One SaaS Suite' }}", "{% if current_lang == 'ru' %}{{ t.features_badge }}{% else %}{{ page.badge|default:t.features_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:t.features|default:'Platform Features' }}", "{% if current_lang == 'ru' %}{{ t.features_title }}{% else %}{{ page.title|default:t.features }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:'Discover all the built-in tools that make Topd the leading fleet and anti-fraud verification engine in Kyrgyzstan.' }}", "{% if current_lang == 'ru' %}{{ t.features_subtitle }}{% else %}{{ page.subtitle|default:t.features_subtitle }}{% endif %}")

    # Feature 1
    c = c.replace('🛡️ Anti-Fraud Verification', '🛡️ {{ t.feat_anti_fraud_badge }}')
    c = c.replace('Check Driver Background Before Handing Over Keys', '{{ t.feat_anti_fraud_h2 }}')
    c = c.replace('Protect your expensive vehicles against dishonest renters. Our unified Anti-Fraud Verification Engine queries a shared regional database of driver histories.', '{{ t.feat_anti_fraud_lead }}')
    c = c.replace('Search by Passport or PIN', '{{ t.feat_search_pin_title }}')
    c = c.replace('Query using passport numbers or official 14-digit national identification numbers.', '{{ t.feat_search_pin_desc }}')
    c = c.replace('7 Critical Incident Classifications', '{{ t.feat_7_incidents_title }}')
    c = c.replace('Flags non-payment, vehicle disappearance, unpaid police fines, contract violations, accidents, and suspicious fraud behavior.', '{{ t.feat_7_incidents_desc }}')
    c = c.replace('5-Star Agency Reputation Rating', '{{ t.feat_reputation_title }}')
    c = c.replace('Check aggregate community ratings and private internal agency comments.', '{{ t.feat_reputation_desc }}')
    c = c.replace('<span>Try Driver Check Tool</span>', '<span>{{ t.try_driver_tool }}</span>')
    c = c.replace('VERIFIED', '{{ t.feat_verified_badge }}')
    c = c.replace('<span class="text-slate-400 text-[10px] uppercase">Safety Score</span>', '<span class="text-slate-400 text-[10px] uppercase">{{ t.safety_score }}</span>')
    c = c.replace('<span class="text-slate-400 text-[10px] uppercase">Fraud Incidents</span>', '<span class="text-slate-400 text-[10px] uppercase">{{ t.fraud_incidents }}</span>')
    c = c.replace('<span>Clean Record — Driver is approved for all vehicle classes.</span>', '<span>{{ t.clean_record_msg }}</span>')

    # Feature 2
    c = c.replace('✍️ Digital Contracts', '✍️ {{ t.feat_contracts_badge }}')
    c = c.replace('Issue Legal Rental Agreements in Under 3 Minutes', '{{ t.feat_wizard_h2 }}')
    c = c.replace('Generate legally sound, customized contracts for any rental scenario without relying on cumbersome paper folders.', '{{ t.feat_wizard_lead }}')
    c = c.replace('5 Supported Contract Modalities', '{{ t.feat_modalities_title }}')
    c = c.replace('Short-Term Rental, Long-Term Rental, Leasing, Installment, and Vehicle Buyout.', '{{ t.feat_modalities_desc }}')
    c = c.replace('Pre-Rental Inspection Photos', '{{ t.feat_inspection_title }}')
    c = c.replace('Record vehicle body condition, scratches, fuel levels, and odometer before handover.', '{{ t.feat_inspection_desc }}')

    # Feature 3
    c = c.replace('🏢 Complete Fleet Control', '🏢 {{ t.feat_fleet_badge }}')
    c = c.replace('Unified Ecosystem for Every Team Member', '{{ t.feat_unified_h2 }}')
    c = c.replace('Topd provides tailored dashboard interfaces for Super Administrators, Rental Companies, and Drivers.', '{{ t.feat_unified_lead }}')
    c = c.replace('Super Admin Master Portal', '{{ t.superadmin_portal_title }}')
    c = c.replace('Full visibility over all subscribers, manual bank payment approvals, user management, and platform-wide website configuration.', '{{ t.superadmin_portal_desc }}')
    c = c.replace('Rental Company Portal', '{{ t.company_portal_title }}')
    c = c.replace('Complete garage fleet management (Available, Rented, Maintenance), agreement creator, driver assignment, and live subscription status.', '{{ t.company_portal_desc }}')
    c = c.replace('Driver Portal', '{{ t.driver_portal_title }}')
    c = c.replace('Drivers can view their active assigned vehicle, review signed contracts, check personal performance ratings, and view incident history.', '{{ t.driver_portal_desc }}')

    # CTA Banner
    c = c.replace('Empower your operations with Topd today', '{{ t.features_cta_title }}')
    c = c.replace('Choose a plan that fits your business or speak with our Bishkek operations team.', '{{ t.features_cta_sub }}')
    c = c.replace('View Plans & Pricing', '{{ t.view_pricing_plans }}')
    c = c.replace('Contact Sales', '{{ t.contact_sales }}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("features.html updated successfully!")


def update_pricing():
    path = r'D:\new\templates\landing\pricing.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'Transparent Pricing' }}", "{% if current_lang == 'ru' %}{{ t.pricing_badge }}{% else %}{{ page.badge|default:t.pricing_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:t.pricing_title|default:'Plans & Subscriptions' }}", "{% if current_lang == 'ru' %}{{ t.pricing_page_title }}{% else %}{{ page.title|default:t.pricing_page_title }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:t.pricing_sub|default:'Choose the right plan for your fleet size with full support for bank transfer, cash, and mobile money.' }}", "{% if current_lang == 'ru' %}{{ t.pricing_page_sub }}{% else %}{{ page.subtitle|default:t.pricing_page_sub }}{% endif %}")

    # Perks in cards
    c = c.replace('<span>Anti-Fraud Driver Check Tool</span>', '<span>{{ t.perk_anti_fraud }}</span>')
    c = c.replace('<span>3-Step Digital Agreement Wizard</span>', '<span>{{ t.perk_wizard }}</span>')
    c = c.replace('<span>Fleet Garage Management</span>', '<span>{{ t.perk_garage }}</span>')
    c = c.replace('<span>Manual Payment & Bank Slip Approval</span>', '<span>{{ t.perk_payments }}</span>')

    # Payment methods
    c = c.replace('Flexible Payment Options Supported', '{{ t.payment_options_title }}')
    c = c.replace('Easy activation through local banking channels in Kyrgyzstan and international wire', '{{ t.payment_options_sub }}')
    c = c.replace('Demir Bank (DKIB)', '{{ t.demir_title }}')
    c = c.replace('Direct wire transfer in USD or KGS Som to our corporate account.', '{{ t.demir_desc }}')
    c = c.replace('Mobile Banking', '{{ t.mobile_bank_title }}')
    c = c.replace('Instant transfer via mBank, Elsom, or regional mobile money.', '{{ t.mobile_bank_desc }}')
    c = c.replace('Cash Deposit', '{{ t.cash_title }}')
    c = c.replace('Hand delivery or cash deposit at our Bishkek office with official receipt.', '{{ t.cash_desc }}')

    # FAQs
    c = c.replace('Got Questions?', '{{ t.faq_badge }}')
    c = c.replace('Frequently Asked Questions', '{{ t.faq_title }}')
    c = c.replace('Everything you need to know about purchasing and managing your Topd subscription.', '{{ t.faq_sub }}')
    c = c.replace('How does subscription purchasing work?', '{{ t.faq_1_q }}')
    c = c.replace(
        'Simply choose your preferred plan on this page, click <strong>"Buy Subscription"</strong>, and you will see our bank transfer and mobile wallet instructions. Complete the transfer through your banking app and submit the transaction reference code. Our operations team verifies and activates your subscription within 15–30 minutes.',
        '{{ t.faq_1_a }}'
    )
    c = c.replace('Can I pay in Kyrgyzstani Som (KGS) or USD?', '{{ t.faq_2_q }}')
    c = c.replace(
        'Yes! Both currencies are fully supported. You can pay via Demir Bank in USD or converted KGS Som using the official daily rate.',
        '{{ t.faq_2_a }}'
    )
    c = c.replace('What is the "Pay Per Check" plan?', '{{ t.faq_3_q }}')
    c = c.replace(
        'The Pay Per Check plan is tailored for occasional rental agencies or individual owners who only need to verify a driver once or twice. Each check costs only $2.00 without requiring a monthly commitment.',
        '{{ t.faq_3_a }}'
    )
    c = c.replace('How do I track my active subscriptions and payment history?', '{{ t.faq_4_q }}')
    c = c.replace(
        'Once logged in, open the <strong>"My Subscription"</strong> page from your dashboard or profile dropdown. You will see live expiration dates, payment receipts, and approval statuses.',
        '{{ t.faq_4_a }}'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("pricing.html updated successfully!")


def update_contact():
    path = r'D:\new\templates\landing\contact.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'Get In Touch' }}", "{% if current_lang == 'ru' %}{{ t.contact_badge }}{% else %}{{ page.badge|default:t.contact_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:t.contact|default:'Contact Us' }}", "{% if current_lang == 'ru' %}{{ t.contact_page_title }}{% else %}{{ page.title|default:t.contact_page_title }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:'Have questions about fleet integration, driver verification, or custom enterprise plans? Our Bishkek team is here to help.' }}", "{% if current_lang == 'ru' %}{{ t.contact_page_sub }}{% else %}{{ page.subtitle|default:t.contact_page_sub }}{% endif %}")

    # Form
    c = c.replace('Send a Message', '{{ t.send_message_badge }}')
    c = c.replace("{{ page.section_title|default:\"We'd Love to Hear From You\" }}", "{% if current_lang == 'ru' %}{{ t.contact_form_title }}{% else %}{{ page.section_title|default:t.contact_form_title }}{% endif %}")
    c = c.replace("{{ page.section_content|default:'Fill out the form below and we will respond within 24 business hours.' }}", "{% if current_lang == 'ru' %}{{ t.contact_form_sub }}{% else %}{{ page.section_content|default:t.contact_form_sub }}{% endif %}")
    c = c.replace('Full Name <span class="text-red-500">*</span>', '{{ t.label_full_name }} <span class="text-red-500">*</span>')
    c = c.replace('Email Address <span class="text-red-500">*</span>', '{{ t.label_email_address }} <span class="text-red-500">*</span>')
    c = c.replace('Phone Number', '{{ t.label_phone_number }}')
    c = c.replace('Your Message <span class="text-red-500">*</span>', '{{ t.label_your_message }} <span class="text-red-500">*</span>')
    c = c.replace('<span>Send Message</span>', '<span>{{ t.btn_send_message }}</span>')

    # Right info box
    c = c.replace('<span>Contact Information</span>', '<span>{{ t.contact_info_box }}</span>')
    c = c.replace('Office Address', '{{ t.office_address }}')
    c = c.replace('Email Support', '{{ t.email_support }}')
    c = c.replace('Phone Support', '{{ t.phone_support }}')
    c = c.replace('Working Hours', '{{ t.working_hours_label }}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("contact.html updated successfully!")


def update_terms():
    path = r'D:\new\templates\landing\terms.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'Legal & Compliance' }}", "{% if current_lang == 'ru' %}{{ t.terms_badge }}{% else %}{{ page.badge|default:t.terms_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:'Terms & Conditions' }}", "{% if current_lang == 'ru' %}{{ t.terms_title }}{% else %}{{ page.title|default:t.terms_title }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:'Last updated: October 2026. Please read these terms carefully before utilizing the Topd platform.' }}", "{% if current_lang == 'ru' %}{{ t.terms_subtitle }}{% else %}{{ page.subtitle|default:t.terms_subtitle }}{% endif %}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("terms.html updated successfully!")


def update_privacy():
    path = r'D:\new\templates\landing\privacy.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Header
    c = c.replace("{{ page.badge|default:'Data Protection' }}", "{% if current_lang == 'ru' %}{{ t.privacy_badge }}{% else %}{{ page.badge|default:t.privacy_badge }}{% endif %}")
    c = c.replace("{{ page.title|default:'Privacy Policy' }}", "{% if current_lang == 'ru' %}{{ t.privacy_title }}{% else %}{{ page.title|default:t.privacy_title }}{% endif %}")
    c = c.replace("{{ page.subtitle|default:'Last updated: October 2026. How Topd collects, safeguards, and handles vehicle and driver verification data.' }}", "{% if current_lang == 'ru' %}{{ t.privacy_subtitle }}{% else %}{{ page.subtitle|default:t.privacy_subtitle }}{% endif %}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("privacy.html updated successfully!")


update_index()
update_about()
update_features()
update_pricing()
update_contact()
update_terms()
update_privacy()
print("ALL TEMPLATES UPDATED SUCCESSFULLY!")

