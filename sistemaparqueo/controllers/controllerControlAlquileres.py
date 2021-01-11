from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View

from sistemaparqueo.models.ModelAlquiler import ModelAlquiler
from sistemaparqueo.models.ModelTarifaAlquiler import ModelTarifaAlquiler
from sistemaparqueo.models.ModelUsuario import ModelUsuario
from sistemaparqueo.models.ModelVehiculo import ModelVehiculo


class MostrarEstadoPagos(TemplateView):
    template_name = 'viewEstadoPagos/contentEstadoPagos.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarEstadoPagos, self).get_context_data(**kwargs)

        obj = ModelUsuario()
        context["usuario"] = obj.buscarUsuarioPorId(kwargs['pk'])

        alquiler=ModelAlquiler()
        context["datos_cliente_alquiler"]=alquiler.buscarAlquilerPorId(kwargs['ak'])
        print(alquiler.listar_cuotas_alquilerPorId(kwargs['ak']))
        context["estado_cuotas"]=alquiler.listar_cuotas_alquilerPorId(kwargs['ak'])
        return context

class MostrarAgregarAlquiler(TemplateView):
    template_name = 'viewAgregarAlquiler.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarAgregarAlquiler, self).get_context_data(**kwargs)

        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(kwargs['pk'])

        vehiculo = ModelVehiculo()
        context["tipo_vehiculos"] = vehiculo.listar_tipo_vehiculos()

        tarifa_alquiler=ModelTarifaAlquiler()
        context["lista_tarifa_alquiler"] = tarifa_alquiler.listar_tarifa_alquiler()

        return context

class BuscarAlquilerPorFiltros(View):
    def get(self,request):
        f_search_ci=request.GET.get('ci')
        alquiler = ModelAlquiler()
        lista_filter_alquiler = alquiler.listarAlquilerPorCiCliente(f_search_ci)
        data = {'lista': lista_filter_alquiler}
        return JsonResponse(data)
