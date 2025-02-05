from django.http import HttpResponse
from rest_framework import generics
from .models import Consulta
from .serializers import ConsultaSerializer

def home(request):
    return HttpResponse("Bem-vindo ao sistema de consultas judiciais!")

class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer