# academics/serializers.py (or fees/serializers.py, depending on your app name)
from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'
