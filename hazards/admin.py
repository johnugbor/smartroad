from django.contrib.gis import admin
from .models import Hazard

@admin.register(Hazard)
class HazardAdmin(admin.GISModelAdmin):
    list_display = ('type', 'status', 'location')