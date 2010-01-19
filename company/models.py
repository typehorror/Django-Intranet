"""
This file is part of Intranet module for Django. This module is
intended to provide a template for profile management.

Copyright (C) 2010  Brice Leroy

Intranet is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Intranet is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Intranet.  If not, see <http://www.gnu.org/licenses/>.
"""
from django.db import models
from common.geo import STATE_CHOICES, COUNTRY_CHOICES

class Company(models.Model):
    title = models.CharField(max_lenght=255)
    description = models.TextField(blank=True)
    logo = models.FileField(upload_to='company_logo')

    # Contact Informations
    phone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)

    # Geographical Address
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=3, choices=STATE_CHOICES, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=4, choices=COUNTRY_CHOICES, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)
