from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from common.utils import xrender
from mechanize import Browser
import hashlib

@login_required
def index(request):
    params = {}
    params.update(csrf(request))
    if request.user.is_authenticated():
        return xrender(request, 'index.html', params)
    else:
        return xrender(request, 'login.html', params)
