from django.db import models


class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=255, default='Topd')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    favicon = models.ImageField(upload_to='site/', blank=True, null=True)
    
    # Contact info
    contact_email = models.EmailField(default='info@topd.kg')
    contact_phone = models.CharField(max_length=50, default='+996 999 083 366')
    address = models.TextField(default='Bishkek, Kyrgyzstan')
    working_hours = models.CharField(max_length=100, default='Monday - Friday: 9:00 AM - 6:00 PM')
    
    # Social links
    facebook_url = models.URLField(blank=True, null=True, default='https://facebook.com')
    twitter_url = models.URLField(blank=True, null=True, default='https://twitter.com')
    instagram_url = models.URLField(blank=True, null=True, default='https://instagram.com')
    linkedin_url = models.URLField(blank=True, null=True, default='https://linkedin.com')

    class Meta:
        verbose_name = 'Website Setting'
        verbose_name_plural = 'Website Settings'

    def __str__(self):
        return self.site_name

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)  # USD, KGS
    name = models.CharField(max_length=50, blank=True)
    symbol = models.CharField(max_length=10, default='$')
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4, default=1.0000)
    is_base = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        ordering = ['-is_base', 'code']

    def __str__(self):
        return f"{self.code} ({self.symbol}) - Rate: {self.exchange_rate}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
