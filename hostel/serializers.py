# academics/serializers.py (or hostel/serializers.py)
from rest_framework import serializers
from .models import Hostel, Room

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    # Optional: show hostel name and student IDs in the response
    hostel_name = serializers.CharField(source='hostel.name', read_only=True)
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hostel', 'hostel_name', 'room_number', 'capacity', 'students']
