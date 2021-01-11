from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView,ListView
from django.views.generic.base import View
from xhtml2pdf import pisa

from db.models import RegistroCaja
from sistemaparqueo.models.ModelDescuento import ModelDescuento
from sistemaparqueo.models.ModelEspacio import ModelEspacio
from sistemaparqueo.models.ModelFactura import ModelFactura
from sistemaparqueo.models.ModelRegistroParqueo import ModelRegistroParqueo

from datetime import datetime

from sistemaparqueo.models.ModelTarifa import ModelTarifa
from sistemaparqueo.models.ModelTarifaRegistro import ModelTarifaRegistro


class MostrarModalDescuentos(TemplateView):
    template_name = 'viewSalidaVehiculos/modalDescuentos.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalDescuentos, self).get_context_data(**kwargs)
        context["id_registro_parqueo"]=kwargs['rpk']

        descuento=ModelDescuento()

        lista_descuentos = descuento.listarDescuentos(kwargs['rpk'])
        context["lista_descuentos"]= lista_descuentos
        return context

class MostrarModalIncidentes(TemplateView):
    template_name = 'viewSalidaVehiculos/modalIncidentes.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarModalIncidentes, self).get_context_data(**kwargs)
        context["id_registro_parqueo"] = kwargs['rpk']

        registro_parqueo = ModelRegistroParqueo()
        lista = registro_parqueo.listarIncidentesporIdRegistro(kwargs['rpk'])
        context["lista_incidentes"]= lista
        return context

class MostrarModalRegistrarSalida(TemplateView):
    template_name = 'viewSalidaVehiculos/modalRegistrarSalida.html'

    def get_context_data(self, **kwargs):

        context = super(MostrarModalRegistrarSalida, self).get_context_data(**kwargs)
        context["id_registro_parqueo"]=kwargs['rpk']

        obj_registro_parqueo=ModelRegistroParqueo()
        registro_entrada = obj_registro_parqueo.buscarRegistroPorId(kwargs['rpk'])
        fecha_entrada = format(registro_entrada["entrada"])
        context["fecha_entrada"] = fecha_entrada

        fecha_salida = format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        context["fecha_salida"] = fecha_salida

        context["id_espacio"]=registro_entrada['id_espacio']

        estancia = obj_registro_parqueo.obtenerHorasYDiasParqueo(fecha_entrada, fecha_salida)
        tarifa = ModelTarifaRegistro()
        precio = tarifa.buscarTarifaPorFechaYHora(estancia['dias'], estancia['horas'])
        context["id_tarifa"] = precio.id_tarifas
        context["precio"] = precio.precio

        verif_alquiler = obj_registro_parqueo.verificarEstadoAlquilerVehiculo(kwargs['rpk'])
        context['estado_alquiler'] = verif_alquiler


        descuento=ModelDescuento()
        sumDescuentos = descuento.buscarDescuentoPorRegistro(kwargs['rpk'])
        if(sumDescuentos[0]["monto"]):
            context["descuento"] = sumDescuentos[0]["monto"]
        else:
            context["descuento"] =0

        context["pagar"] = precio.precio - context["descuento"]
        #print (context)
        return context

class RegistrarSalida(View):
    def get(self, request):

        f_id_registro = request.GET.get('id_registro')
        f_fecha_salida=request.GET.get('fecha_salida')
        f_id_tarifa = request.GET.get('id_tarifa')
        f_id_espacio = request.GET.get('idEspacio')
        f_monto = request.GET.get('monto')
        print (request.GET)

        registro = ModelRegistroParqueo()
        isAlquiler = registro.verificarEstadoAlquilerVehiculo(f_id_registro)

        if(isAlquiler):
            registro_parqueo = ModelRegistroParqueo()
            registro_parqueo.set_salida(f_fecha_salida)
            registro_parqueo.registrarSalidaAlquiler(f_id_registro)

            espacio = ModelEspacio()
            espacio.set_estado('DISPONIBLE')
            espacio.actualizarEstado(f_id_espacio)

        else:
            registro_parqueo = ModelRegistroParqueo()
            registro_parqueo.set_salida(f_fecha_salida)
            registro_parqueo.registrarSalida(f_id_registro, f_id_tarifa, float(f_monto))

            espacio = ModelEspacio()
            espacio.set_estado('DISPONIBLE')
            espacio.actualizarEstado(f_id_espacio)

        descuento=ModelDescuento()
        is_descuento = descuento.isDescuento(f_id_registro)

        recibo =ModelFactura()
        recibo.agregarReciboSalidaVehiculo(f_id_registro)


        data = {"id_registro":f_id_registro}
        return JsonResponse(data)

class ImprimirTicketSalida(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        template = get_template('reportes/templete_tickets_salida.html')
        registro = ModelRegistroParqueo()
        isAlquiler = registro.verificarEstadoAlquilerVehiculo(kwargs['rpk'])
        datos_registro = registro.obtenerDatosParaTicket(kwargs['rpk'])
        print(datos_registro)
        if(not isAlquiler):

            descuento = ModelDescuento()
            sumDescuentos = descuento.buscarDescuentoPorRegistro(kwargs['rpk'])

            tarifa = ModelTarifaRegistro()
            print("EL ID TARIFA ES")
            print(datos_registro['id_tarifas'])
            obj_tarifa = tarifa.buscarTarifaPorId(datos_registro['id_tarifas'])
            print("EL PRECIO ES")
            print(obj_tarifa.precio)

            if (sumDescuentos[0]["monto"]):
                total_descuentos  = sumDescuentos[0]["monto"]
            else:
                total_descuentos = 0
            total = obj_tarifa.precio - total_descuentos
            context = {"datos_registro": datos_registro, "precio": obj_tarifa.precio, "descuentos": total_descuentos,
                       "total": total, "isAlquiler":isAlquiler}

        else:
            print ("EL VEHICULO TIENE ALQUILER")
            context = {"datos_registro": datos_registro,"isAlquiler":isAlquiler}

        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ticket_salida.pdf"'

        pisStatus = pisa.CreatePDF(
            html, dest=response
        )
        if pisStatus.err:
            return HttpResponse("OCURRIO UN ERROR")
        return response

class RegistrarDescuento(View):
    def get(self, request):
        f_monto = request.GET.get('monto')
        f_descripcion = request.GET.get('descripcion')
        f_id_parqueo = request.GET.get('id_parqueo')
        descuento = ModelDescuento()
        descuento.set_monto(f_monto)
        descuento.set_descripcion(f_descripcion)
        descuento.registrarDescuentos(f_id_parqueo)
        data = {}
        return JsonResponse(data)

class RegistrarIncidente(View):
    def get(self,request):
        f_id_parqueo=request.GET.get('id_parqueo')
        f_descripcion=request.GET.get('descripcion')

        registro=ModelRegistroParqueo()
        registro.registrarIncidentes(f_id_parqueo, f_descripcion)

        data = {}
        return JsonResponse(data)

class VerificarEstadoAlquilerRegistro(View):
    def get(self,request):
        f_id_parqueo=request.GET.get('id_parqueo')

        registro = ModelRegistroParqueo()
        isAlquiler =  registro.verificarEstadoAlquilerVehiculo(f_id_parqueo)
        data = {"verif_alquiler":isAlquiler}
        return JsonResponse(data)

class BuscarVehiculoPorFiltro(View):
    def get(self,request):
        f_placa = request.GET.get('placa')
        registro=ModelRegistroParqueo()
        lista = registro.listarVehiculosConEntradaRegistradaPorPlaca(f_placa)
        print(lista)

        data = {'lista':lista}
        return JsonResponse(data)






