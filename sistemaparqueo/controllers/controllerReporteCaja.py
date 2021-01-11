from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from sistemaparqueo.models.ModelAdministrador import ModelAdministrador

class FiltrosReporteCaja(View):

    def get(self,request):
        f_mes = request.GET.get('mes')

        adm=ModelAdministrador()
        results=adm.mostrarReporteCajaConFiltros(f_mes)
        lista_total=adm.mostrarTotalReporteCajaConFiltros(f_mes)
        print(lista_total)

        data={'lista':results,'sumtotal':lista_total}
        return JsonResponse(data)