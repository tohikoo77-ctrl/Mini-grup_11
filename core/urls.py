from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('schema-viewer/', include('schema_viewer.urls')),
    path('rosetta/', include('rosetta.urls')),

    # DRF schema and documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # DRF auth
    path('api-auth/', include('rest_framework.urls')),

    # Your app endpoints
    path('accounts/', include('apps.accounts.urls')),
]

# Serve media and static files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
