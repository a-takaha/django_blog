from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("mysns/", include("mysns.urls")),
    path('admin/', admin.site.urls),
]
