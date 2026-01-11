from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth Routes (Login, Signup, Google, Facebook)
    path('api/auth/', include('users.urls')),
    
    # App Routes
    path('api/hazards/', include('hazards.urls')),
    
    # Social Login Routes (Required by allauth)
    path('accounts/', include('allauth.urls')),
]