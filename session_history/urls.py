from django.contrib import admin
from django.urls import path, include

from session_history.views import index, about

urlpatterns = [

    # feature urls
    path('index', index, name='session_history'),
    path('about', about, name='about_page'),
    path('', admin.site.urls),

]