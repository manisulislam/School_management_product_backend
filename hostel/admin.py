from django.contrib import admin
from .models import Hostel, Room

# ✅ Register Hostel
@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ("name", "warden_name", "capacity")
    search_fields = ("name", "warden_name")
    list_filter = ("capacity",)

# ✅ Register Room
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("hostel", "room_number", "capacity")
    search_fields = ("hostel__name", "room_number")
    list_filter = ("capacity",)
    filter_horizontal = ("students",)  # ✅ allows selecting students via a horizontal filter widget
