from django.urls import path, include

urlpatterns = [
    # This automatically sets up: /login/, /logout/, /password-reset/, etc.
    path('', include('dj_rest_auth.urls')),
    
    # Registration endpoints
    path('registration/', include('dj_rest_auth.registration.urls')),
]