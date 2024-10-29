from django.contrib import admin
from django.urls import path
from privet.views import get_hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path('privet/', get_hello)
]
