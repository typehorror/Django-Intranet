"""
This file is part of Profile module for Django. This module is
intended to provide a template for profile management.

Copyright (C) 2010  Brice Leroy

Profile is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Profile is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Profile.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.utils.hashcompat import sha_constructor
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, REDIRECT_FIELD_NAME, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site, RequestSite

# favour django-mailer but fall back to django.core.mail
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail

from profile.settings import DEFAULT_EMAIL_FROM

from profile.forms import LoginForm, ProfileForm, UserForm, SetPasswordForm
from common.shortcuts import render_response, render_string
from profile.models import Profile
    
def login_view(request, template_name='login.html', redirect_field_name=REDIRECT_FIELD_NAME):
    """
    This version of login view allow the user to connect using his email and password.
    """
    context = {}
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Light security check -- make sure redirect_to isn't garbage.
            if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL
            login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        form = LoginForm(request)
    request.session.set_test_cookie()
    return render_response(request,template_name, {
        'login_form': form,
    })
login_view = never_cache(login_view)

@login_required
def thank_you_for_registering(request, template_name='thank_you_for_registering.html', redirect_field_name=REDIRECT_FIELD_NAME):
    """
    This function exist for the user to be redirected so it can be logged 
    as a rechead goal for analytics. (see goals in google analytics)
    This page appear just once if the session variable "first_login" is defined.
    If it's not it's first login, the user will be directly redirect to GET['next'] 
    value or the default LOGIN_REDIRECT_URL (defined in settings.py)
    """
    if request.session.has_key('first_login'):
        del request.session['first_login']
        return render_response(request, template_name)
    else:
        redirect_to = request.REQUEST.get(redirect_field_name, '')
        if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL
        return HttpResponseRedirect(redirect_to)

@login_required
def profile_view(request, template_name='profile_form.html'):
    """
    Allow user to add personnal data to his profile
    if the profile is saved, a context variable profile_saved is set to True
    """
    profile = request.user.get_profile()
    context = {}
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        user_form = UserForm(instance=request.user, data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            context['profile_saved'] = True
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    context.update({'user_form': user_form,
                    'profile_form': profile_form,
                    'current':'account'})
    return render_response(request, template_name, context)

@login_required
def password_view(request, template_name='password_form.html'):
    """
    Allow user to change his password by entering his old one
    if the password is saved, a context variable password_saved is set to True
    """
    profile = request.user.get_profile()
    context = {}
    if request.method == "POST":
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            context['password_saved'] = True
    else:
        password_form =PasswordChangeForm(user=request.user)
    context.update({'password_form': password_form})
    return render_response(request, template_name, context)
password_view = never_cache(password_view)
    
@login_required
def logout_view(request):
    """
    disconnect the current user.
    """
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(reverse('login_view'))
