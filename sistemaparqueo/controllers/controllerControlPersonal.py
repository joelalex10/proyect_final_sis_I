from django.http import JsonResponse
from django.views import View

from sistemaparqueo.models.ModelEmpleado import ModelEmpleado
from sistemaparqueo.models.ModelUsuario import ModelUsuario

class BuscarPorFiltros(View):
    def get(self,request):
        f_ci_usuario = request.GET.get('ciUsuario')
        f_fecha = request.GET.get('Fecha')

        if(f_ci_usuario and f_fecha):
            empleado = ModelEmpleado()
            empleado.set_ci(f_ci_usuario)
            lista = empleado.listarEntradaDeEmpleados_filtro_Ci_Fecha(f_fecha)
            print(lista)
        elif(f_ci_usuario):
            empleado = ModelEmpleado()
            empleado.set_ci(f_ci_usuario)
            lista=empleado.listarEntradaDeEmpleados_filtroCi()
            print(lista)
        elif(f_fecha):
            empleado = ModelEmpleado()
            lista = empleado.listarEntradaDeEmpleados_filtroFecha(f_fecha)
            print(lista)

        data = {"lista":lista}

        return JsonResponse(data)