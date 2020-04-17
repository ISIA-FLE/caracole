#!/usr/bin/python3

from django.contrib import admin
from . import models as m


admin.site.register((m.AdminMessage, m.Network, m.Subgroup, m.Delivery, m.Product, m.Purchase, m.Plural, m.UserPhones, m.ProductDiscrepancy, m.Candidacy))
