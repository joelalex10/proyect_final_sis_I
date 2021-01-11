from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from sistemaparqueo.models.ModelTarifaAlquiler import ModelTarifaAlquiler
from sistemaparqueo.models.ModelTarifaRegistro import ModelTarifaRegistro


class AgregarTarifas(View):
    def get(self, request):
        f_horas=request.GET.get('hora')
        f_dias = request.GET.get('dia')
        f_precio = request.GET.get('precio')

        tarifa_registro=ModelTarifaRegistro()
        tarifa_registro.set_hora(f_horas)
        tarifa_registro.set_monto(f_precio)
        tarifa_registro.set_dia(f_dias)
        tarifa_registro.agregar_tarifa_registro()
        data = {}
        return JsonResponse(data)

class AgregarTarifaAlquiler(View):
    def get(self, request):
        f_mes=request.GET.get('mes')
        f_precio = request.GET.get('precio')
        tarifa_alquiler=ModelTarifaAlquiler()
        tarifa_alquiler.set_monto(f_precio)
        tarifa_alquiler.set_mes(f_mes)
        tarifa_alquiler.agregar_tarifa_alquiler()
        data = {}
        return JsonResponse(data)

class MostrarModalTarifaRegistro(TemplateView):
    template_name = 'viewGestionDeTarifas/modalEditarTarifaRegistro.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalTarifaRegistro, self).get_context_data(**kwargs)
        print("LA LLAVE ES")
        print(kwargs['pk'])
        obj = ModelTarifaRegistro()
        tarifa_id=obj.buscarTarifaPorId(kwargs['pk'])
        context["tarifa"]=tarifa_id
        return context

class EditarTarifaRegistro(View):
    def get(self,request):
        f_id = request.GET.get("id")
        f_horas = request.GET.get("horas")
        f_dias = request.GET.get("dias")
        f_precio = request.GET.get("precio")

        obj = ModelTarifaRegistro()
        obj.set_dia(f_dias)
        obj.set_hora(f_horas)
        obj.set_monto(f_precio)
        obj.actualizarTarifaRegistro(f_id)
        data={}
        return JsonResponse(data)

class MostrarModalTarifaAlquiler(TemplateView):
    template_name = "viewGestionDeTarifas/modalEditarTarifaAlquiler.html"
    def get_context_data(self, **kwargs):
        context = super(MostrarModalTarifaAlquiler, self).get_context_data(**kwargs)
        obj = ModelTarifaAlquiler()
        tarifa_id=obj.buscarTarifaAlquilerPorId(kwargs['pk'])
        context["tarifa_alquiler"]=tarifa_id
        return context
class EditarTarifaAlquiler(View):
    def get(self,request):
        f_id_a = request.GET.get("id")
        f_meses = request.GET.get("meses")
        f_precio = request.GET.get("precio")
        obj = ModelTarifaAlquiler()
        obj.set_mes(f_meses)
        obj.set_monto(f_precio)
        obj.actualizarTarifaAlquiler(f_id_a)
        data={}
        return JsonResponse(data)

