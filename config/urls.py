from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is imported here
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # <-- Add this line to route traffic to your app
]


# This line tells Django to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)