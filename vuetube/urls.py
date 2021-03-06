from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/register/', include('rest_auth.registration.urls')),
]
