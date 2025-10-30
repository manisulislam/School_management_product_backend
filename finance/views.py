# academics/views.py (or fees/views.py)
from rest_framework import viewsets, filters
from .models import Fee
from .serializers import FeeSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__name', 'is_paid']  
