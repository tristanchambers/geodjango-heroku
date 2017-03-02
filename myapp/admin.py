from django.contrib import admin
from myapp.models import Icecream
from django.contrib.gis import admin

admin.site.register(Icecream, admin.OSMGeoAdmin)
