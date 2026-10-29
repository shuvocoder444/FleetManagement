import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from apps.site_settings.models import FrontendPage

pages_data = [
    {
        'slug': 'home',
        'title': 'Complete Fleet Management and Driver Verification Ecosystem',
        'badge': "Central Asia's First Unified Platform",
        'subtitle': 'Protect your car rental fleet from fraud, unpaid fines, and vehicle damage. Instant blacklist background checks, automated legal digital agreements, and smart fleet maintenance.',
        'section_title': 'Verified Anti-Fraud Driver Check',
        'section_content': "Connect your fleet to Kyrgyzstan's most comprehensive car rental anti-fraud network. Instantly screen drivers for active court warrants, unpaid damage disputes, and blacklisted behavior.",
    },
    {
        'slug': 'about',
        'title': 'About Us',
        'badge': 'Our Mission and Platform',
        'subtitle': 'Building the most reliable, unified digital fleet ecosystem and driver anti-fraud network for Kyrgyzstan and Central Asia.',
        'section_title': 'Empowering Car Rental Companies With Technology and Trust',
        'section_content': 'Vehicle rental operations have traditionally suffered from paper-heavy agreements, untracked vehicle handovers, and high risks of fraud, unpaid fines, or vehicle disappearance. Topd was engineered from the ground up to eliminate these risks. We provide a single cloud platform where fleet owners, rental companies, and leasing operators can verify drivers against unified blacklist data, generate legally enforceable contracts with pre-rental condition photos, and automate payments.',
    },
    {
        'slug': 'features',
        'title': 'Platform Features',
        'badge': 'Enterprise Capabilities',
        'subtitle': 'Everything you need to run, protect, and scale car rental operations in Kyrgyzstan.',
        'section_title': 'Anti-Fraud Driver Check and Digital Agreements',
        'section_content': 'Topd provides an end-to-end suite engineered for automotive leasing and rental companies in Bishkek and Central Asia. From instant PIN/Passport lookups to pre-rental condition photo logging and automated garage maintenance tracking.',
    },
    {
        'slug': 'pricing',
        'title': 'Transparent, Scalable Pricing',
        'badge': 'Affordable Fleet Safety',
        'subtitle': 'Choose the ideal plan for your rental agency. Pay per verification or enjoy unlimited access with enterprise priority support.',
        'section_title': 'Direct Bank Wire and Mobile Wallet Transfers',
        'section_content': 'We accept local payments via Demir Kyrgyz International Bank (DKIB), MBank, and Optima Bank. All transactions are reviewed and approved by our billing administrators within 30 minutes.',
    },
    {
        'slug': 'contact',
        'title': 'Contact Us',
        'badge': 'Get In Touch',
        'subtitle': 'Have questions about fleet integration, driver verification, or custom enterprise plans? Our Bishkek team is here to help.',
        'section_title': "We'd Love to Hear From You",
        'section_content': 'Fill out the form below and we will respond within 24 business hours.',
    },
    {
        'slug': 'terms',
        'title': 'Terms and Conditions',
        'badge': 'Legal and Compliance',
        'subtitle': 'Last updated: October 2026. Please read these terms carefully before utilizing the Topd platform.',
        'section_title': 'Platform Rules and Governing Law',
        'section_content': 'Full legal terms governing usage of Topd SaaS fleet solutions in the Kyrgyz Republic.',
    },
    {
        'slug': 'privacy',
        'title': 'Privacy Policy',
        'badge': 'Security and Trust',
        'subtitle': 'Last updated: October 2026. How Topd collects, safeguards, and handles your business and driver data.',
        'section_title': 'Data Protection and Driver Rights',
        'section_content': 'Clear rules regarding personal data handling, driver records, and secure storage.',
    },
]

for p in pages_data:
    obj, created = FrontendPage.objects.get_or_create(slug=p['slug'], defaults=p)
    if not created:
        for k, v in p.items():
            setattr(obj, k, v)
        obj.save()
    print(f"Page {obj.slug} (ID: {obj.id}): created={created}, title={obj.title}")

print("Seeding completed successfully!")
