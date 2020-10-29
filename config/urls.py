
from django.contrib import admin
from django.urls import path, include

v1 = [
    path('v1/', include('apps.user.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1)),
]