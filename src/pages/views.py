import os
import sys

from django import get_version
from django.conf import settings
from django.shortcuts import render
from .models import Computadora, SistemaOperativo


def home(request):
    pc=Computadora("Dell", 16)
    so=SistemaOperativo("Linux", "Ubuntu 22.04")
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": sys.version,
        "pc": pc,
        "so": so,
    }

    return render(request, "pages/home.html", context)
