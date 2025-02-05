from django.urls import path
from .views import ConsultaListCreateView, home

urlpatterns = [
    path('', home, name='home'),  # Rota para a página inicial
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
]