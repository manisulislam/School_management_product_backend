
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/academics/', include('academics.urls')), 
    path('api/common/', include('common.urls')), 
    path('api/finance/', include('finance.urls')), 
    path('api/hostel/', include('hostel.urls')), 
    path('api/library/', include('library.urls')), 
    path('api/students/', include('students.urls')), 
    path('api/transport/', include('transport.urls')), 
    path('api/users/', include('users.urls')), 


]
