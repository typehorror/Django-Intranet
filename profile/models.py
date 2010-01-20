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
from django.utils.translation import ugettext as _

from django.db import models
from django.contrib.auth.models import User

from common.geos import COUNTRY_CHOICES, STATE_CHOICES

SEX_CHOICES = (
    ('male', _('Male')),
    ('female', _('Female')),
)

class Profile(models.Model):
    """
    A profile store data linked to a user. It allows you
    to extend the data model and functionality.
    """
    # User link (one to one relation)
    user = models.ForeignKey(User, related_name='profile', unique=True, editable=False)
    company = models.ForeignKey('company.Company', related_name='company', unique=True)
    sex = models.CharField(_('Gender'), max_length=6, choices=SEX_CHOICES, blank=True)
    birth_date = models.DateField(blank=True, null=True, help_text=_("format: yyyy-mm-dd"))
    
    picture = models.FileField(upload_to='profile_picture')

    # Contact Informations
    phone = models.CharField(max_length=20, blank=True)
    cell = models.CharField(max_length=20, blank=True)
    extension = models.CharField(max_length=20, blank=True)

    # Geographical Address
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=4, choices=COUNTRY_CHOICES, blank=True)
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('profile.views.profile_detail', [self.pk])
