from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from core.views import index_view
urlpatterns = [
    path('account/',include('account.urls', namespace="account")),
    path('core/',include('core.urls', namespace="core")),
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)