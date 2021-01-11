from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from sistemaparqueo.models.ModelDescuento import ModelDescuento
from sistemaparqueo.models.ModelRegistroParqueo import ModelRegistroParqueo


class MostrarModalIncidentes(TemplateView):
    template_name = 'viewHistorialUbicacion/modalHistorialIncidentes.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalIncidentes, self).get_context_data(**kwargs)
        print(kwargs['pki'])

        #descuento=ModelDescuento()
        #lista=descuento.listarDescuentos(kwargs['pki'])
        #print(lista)

        registro=ModelRegistroParqueo()
        lista=registro.listarIncidentesporIdRegistro(kwargs['pki'])
        context['lista_incidentes']=lista
        return context

class MostrarModalDescuentos(TemplateView):
    template_name = 'viewHistorialUbicacion/modalHistorialDescuentos.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalDescuentos, self).get_context_data(**kwargs)

        descuento=ModelDescuento()
        lista=descuento.listarDescuentos(kwargs['pki'])
        context['lista_descuentos']=lista
        print(lista)
        return context

class MostrarDetalles(TemplateView):
    template_name = 'viewHistorialUbicacion/modalDetalles.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarDetalles, self).get_context_data(**kwargs)
        registro=ModelRegistroParqueo()

        datos = registro.buscarRegistroPorIdParaHistorial(kwargs['pki'])
        posicion = int(datos['posicion'])
        sector = datos['sector']
        entrada = datos['entrada'].strftime("%Y-%m-%d %H:%M:%S")
        salida = datos['salida'].strftime("%Y-%m-%d %H:%M:%S")

        registro_parqueo = ModelRegistroParqueo()
        lista_izquierda = registro_parqueo.buscarRegistroEntradasPorDetalles(entrada, salida, sector,(posicion - 1))
        lista_derecha = registro_parqueo.buscarRegistroEntradasPorDetalles(entrada, salida, sector,(posicion + 1))
        context['lista_izquierda']=lista_izquierda
        context['lista_derecha']=lista_derecha

        lista_izquierda = registro_parqueo.buscarRegistroSalidasPorDetalles(entrada, salida, sector, (posicion - 1))
        lista_derecha = registro_parqueo.buscarRegistroSalidasPorDetalles(entrada, salida, sector, (posicion + 1))
        context['lista_izquierda_salida'] = lista_izquierda
        context['lista_derecha_salida'] = lista_derecha

        return context

class BuscarHistorialPorFiltros(View):
    def get(self,request):
        f_fecha=request.GET.get('fecha')
        f_placa=request.GET.get('placa')
        if(f_fecha and f_placa ):
            registro = ModelRegistroParqueo()
            lista = registro.listarVehiculosConSalidaRegistradaPorFechaYPlaca(f_fecha,f_placa)
            print(lista)
        elif(f_fecha):
            registro = ModelRegistroParqueo()
            lista = registro.listarVehiculosConSalidaRegistradaPorFecha(f_fecha)
            print(lista)
        elif(f_placa):
            registro = ModelRegistroParqueo()
            lista = registro.listarVehiculosConSalidaRegistradaPorPlaca(f_placa)
            print(lista)

        data = {"lista":lista}
        return JsonResponse(data)





