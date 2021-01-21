from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Funcionario


#def home(request):
    #return HttpResponse('Hello!')



class FuncionarioList(ListView):
    model = Funcionario
    #fields = ['nome',]

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)





''' def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()

        return HttpResponse('OK')'''