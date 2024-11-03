# urls.py

from django.urls import path

from naturezen_core.ajax_controller.ajax_controller import update_bpm

urlpatterns = [
    path('update-bpm', update_bpm, name='update_bpm'),
]
