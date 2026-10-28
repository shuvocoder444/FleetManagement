from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.site_settings.urls')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('vehicles/', include('apps.vehicles.urls', namespace='vehicles')),
    path('drivers/', include('apps.drivers.urls', namespace='drivers')),
    path('agreements/', include('apps.agreements.urls', namespace='agreements')),
    path('billing/', include('apps.billing.urls', namespace='billing')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
