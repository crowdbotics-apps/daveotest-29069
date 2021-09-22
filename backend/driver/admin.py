from django.contrib import admin
from .models import DriverProfile, DriverOrder

admin.site.register(DriverOrder)
admin.site.register(DriverProfile)

# Register your models here.
