from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sessions/', include('session_history.urls')),
    path('bpm/', include('naturezen_core.urls')),
    path('', admin.site.urls),
]
