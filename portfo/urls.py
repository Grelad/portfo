"""portfo URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('portfo.apps.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('portfo.apps.portfolio.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)