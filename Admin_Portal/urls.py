# Admin_Portal/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('Users/', include('Users.urls')),
    path('Users/', include('django.contrib.auth.urls')),
]
