from rest_framework import serializers
from .models import BusRoute, BusAssignment

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = "__all__"


class BusAssignmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.name", read_only=True)
    route_name = serializers.CharField(source="route.route_name", read_only=True)

    class Meta:
        model = BusAssignment
        fields = ["id", "student", "student_name", "route", "route_name", "pickup_point"]
