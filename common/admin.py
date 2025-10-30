from django.contrib import admin
from .models import Inventory, HealthRecord

# ✅ Register Inventory
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("item_name", "quantity", "purchase_date", "assigned_to")
    search_fields = ("item_name", "assigned_to__name")
    list_filter = ("purchase_date",)

# ✅ Register HealthRecord
@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ("student", "blood_group", "emergency_contact")
    search_fields = ("student__first_name", "student__last_name", "blood_group")
    list_filter = ("blood_group",)
