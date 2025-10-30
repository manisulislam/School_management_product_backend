from django.contrib import admin
from .models import BusRoute, BusAssignment

# ✅ Register BusRoute
@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ("route_name", "bus_number", "driver_name", "driver_phone")
    search_fields = ("route_name", "bus_number", "driver_name")
    list_filter = ("route_name",)

# ✅ Register BusAssignment
@admin.register(BusAssignment)
class BusAssignmentAdmin(admin.ModelAdmin):
    list_display = ("student", "route", "pickup_point")
    search_fields = ("student__first_name", "student__last_name", "route__route_name")
    list_filter = ("route",)
