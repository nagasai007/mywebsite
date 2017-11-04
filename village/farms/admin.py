# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from django.contrib import admin
from .models import house_hold,persons_info,farm_info,season_info,well_info,well_observation,crops,farm_yield

admin.site.register(house_hold)
admin.site.register(persons_info)
admin.site.register(farm_info)
admin.site.register(farm_yield)
admin.site.register(season_info)
admin.site.register(crops)
admin.site.register(well_info)
admin.site.register(well_observation)
