
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/academics/', include('academics.urls')), 
    path('api/common/', include('common.urls')), 
    path('api/finance/', include('finance.urls')), 
]
