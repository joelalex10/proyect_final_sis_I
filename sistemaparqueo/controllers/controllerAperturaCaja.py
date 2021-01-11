from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView,ListView

from sistemaparqueo.models.ModelCaja import ModelCaja
from sistemaparqueo.models.ModelEmpleado import ModelEmpleado


class CalcularTotal(View):
    def get(self,request):
        total=request.GET.get('total')
        caja=ModelCaja()
        literal = caja.convertirLiteralMonto(float(total))

        data = {'literal':literal}
        return JsonResponse(data)

class AbrirModalConfirmacion(TemplateView):
    template_name = 'viewAperturaCaja/modalConfirmacion.html'

    def get_context_data(self, **kwargs):
        context = super(AbrirModalConfirmacion, self).get_context_data(**kwargs)
        context["id_usuario"]=kwargs['pk']
        return context




class VerificarEstadoCaja(View):
    def get(self,request):
        caja =ModelCaja()
        caja.set_estado("ACTIVO")
        estado = caja.verificarEstadoCaja()
        if(not estado):
            data={"confirm":True}
        else:
            data = {}
        return JsonResponse(data)

class RegistrarApertura(View):
    def get(self,request):
        f_hora_apertura=request.GET.get("hora_apertura")
        f_monto_apertura=request.GET.get("monto_apertura")
        f_id_usuario=request.GET.get("id_usuario")
        f_fecha = request.GET.get("fecha")

        caja=ModelCaja()
        caja.set_hora_entrada(f_hora_apertura)
        caja.set_monto_apertura(f_monto_apertura)
        caja.set_estado("ACTIVO")
        caja.set_fecha(f_fecha)
        caja.registrarAperturaCaja(f_id_usuario)

        empleado = ModelEmpleado()
        empleado.registrarHorarioEntrada(f_fecha,f_hora_apertura,f_id_usuario)

        data = {}
        return JsonResponse(data)



