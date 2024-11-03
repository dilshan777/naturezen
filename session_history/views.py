import json

from bson import ObjectId
from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from naturezen_core.models import BPMRecord


def index(request):
    breadcrumb = []
    context = {
        'available_apps': admin.site.get_app_list(request),
        'breadcrumbs': breadcrumb,
        'session_history': BPMRecord.objects.filter(username=request.user.username)
    }

    return render(request, 'all_session.html', context)


