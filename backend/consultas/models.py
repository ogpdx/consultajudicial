from django.db import models

class Consulta(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    resultado = models.JSONField(default=dict)  # Armazena os resultados da consulta
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta para {self.cpf}"