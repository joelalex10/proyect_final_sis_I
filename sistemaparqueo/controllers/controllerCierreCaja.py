from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View

from sistemaparqueo.models.ModelCaja import ModelCaja
from sistemaparqueo.models.ModelEmpleado import ModelEmpleado


class MostrarModalConfirmacion(TemplateView):

    template_name = 'viewCierreCaja/modalCierreCaja.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarModalConfirmacion, self).get_context_data(**kwargs)

        context["id_usuario"]=kwargs['pk']
        return context




class RegistrarClausura(View):
    def get(self,request):
        f_hora_clausura=request.GET.get("hora_clausura")
        f_monto_clausura=request.GET.get("monto_clausura")
        print(f_hora_clausura)
        print(f_monto_clausura)
        caja = ModelCaja()
        caja.set_estado("ACTIVO")
        id_caja_abierta = caja.verificarEstadoCaja()[0]['id_registro_caja']

        caja.set_monto_cierre(float(f_monto_clausura))
        caja.set_hora_cierre(f_hora_clausura)
        caja.set_estado("CERRADO")
        caja.registrarCierreCaja(id_caja_abierta)

        empleado=ModelEmpleado()
        empleado.registrarHorarioSalida(f_hora_clausura)

        data = {}
        return JsonResponse(data)
