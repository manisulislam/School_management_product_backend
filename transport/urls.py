from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusRouteViewSet, BusAssignmentViewSet

router = DefaultRouter()
router.register(r'bus-routes', BusRouteViewSet)
router.register(r'bus-assignments', BusAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
