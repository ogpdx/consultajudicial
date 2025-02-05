from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('consultas.urls')),  # Inclui as URLs da aplicação consultas
]