from django.contrib import admin
from django.urls import path
from app.views import get_hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_hello)
]
