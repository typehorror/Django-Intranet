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

from django.conf.urls.defaults import *

urlpatterns = patterns('profile.views',
    url(r'^login/$', 'login_view', name='login_view'),
    url(r'^logout/$', 'logout_view', name='logout_view'),
    url(r'^me/$', 'profile_view', name='profile_view'),
    url(r'^password/$', 'password_view', name='password_view'),
    url(r'^thank_you/$', 'thank_you_for_registering', name='thank_you_for_registering'),
)

urlpatterns += patterns('',
    url(r'^new_account/confirm/$', 'django.views.generic.simple.direct_to_template', {'template':'profile/new_account_confirm.html'}, name='profile_new_account_confirm'),
)
