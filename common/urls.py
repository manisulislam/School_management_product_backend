from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, HealthRecordViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
router.register(r'health-records', HealthRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
