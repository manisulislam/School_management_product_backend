from rest_framework import viewsets, permissions
from .models import BusRoute, BusAssignment
from .serializers import BusRouteSerializer, BusAssignmentSerializer

class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BusAssignmentViewSet(viewsets.ModelViewSet):
    queryset = BusAssignment.objects.select_related("student", "route").all()
    serializer_class = BusAssignmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
