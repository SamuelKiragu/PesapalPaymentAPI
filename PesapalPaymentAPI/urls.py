from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    'rest_framework',
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
