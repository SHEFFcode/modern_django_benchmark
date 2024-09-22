# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # Add this line to include your API
]
