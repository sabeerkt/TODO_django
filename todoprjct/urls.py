from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    # Other URL patterns for the project go here
]
