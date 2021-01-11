from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView,ListView

from sistemaparqueo.models.ModelAlquiler import ModelAlquiler


class MostrarModalEstadoPagos(TemplateView):
    template_name = 'viewReporteAlquileres/modalEstadoPagos.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalEstadoPagos, self).get_context_data(**kwargs)

        alquiler = ModelAlquiler()
        context["estado_cuotas"] = alquiler.listar_cuotas_alquilerPorId(kwargs['ak'])

        return context

class BuscarPorFiltros(View):
    def get(self,request):
        f_search_ci=request.GET.get('ci')
        print("EL CI DE FILTRO ES: "+f_search_ci)
        alquiler=ModelAlquiler()
        lista_filter_alquiler=alquiler.listarAlquilerPorCiCliente(f_search_ci)
        data = {'lista':lista_filter_alquiler}
        return JsonResponse(data)