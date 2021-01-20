from django.db import models
from django.contrib.auth.models import User
from apps.funcionarios.models import Funcionario



class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Nome da Empresa')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo

