from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),

    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),


]
