from django.contrib import admin
from django.urls import path, include

from session_history.views import index

urlpatterns = [

    # feature urls
    path('index', index, name='session_history'),
    path('', admin.site.urls),

]