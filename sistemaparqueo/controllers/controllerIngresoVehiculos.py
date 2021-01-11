from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from sistemaparqueo.models.ModelEspacio import ModelEspacio
from sistemaparqueo.models.ModelRegistroParqueo import ModelRegistroParqueo
from sistemaparqueo.models.ModelVehiculo import ModelVehiculo
from datetime import datetime

import os

class BuscarPlacaAlquiler(View):
    def get(self,request):
        f_placa = request.GET.get('placa')
        vehiculo = ModelVehiculo()
        vehiculo.set_placa(f_placa)
        variable = vehiculo.buscarVehiculoPorPlaca_only()

        if(variable):
            data = {'vehiculoAlquiler': variable[0]}
        else:
            data = {}
        return JsonResponse(data)

class RegistrarEntrada(View):
    def get(self,request):

        f_id_espacio = request.GET.get('idEspacio')
        f_id_placa = request.GET.get('idPlaca')
        f_id_tipo_vehiculo = request.GET.get('idTipoVehiculo')
        f_placa = request.GET.get('placa')
        f_color = request.GET.get('color')
        f_id_usuario = request.GET.get('usuario')
        fi_id_placa = int(f_id_placa)

        if (fi_id_placa != 0):
            registro_entrada = ModelRegistroParqueo()
            registro_entrada.set_entrada(format(datetime.now()))
            new_id_registro = registro_entrada.registrarEntrada(f_id_usuario, f_id_placa, f_id_espacio)

            espacio = ModelEspacio()
            espacio.set_estado("OCUPADO")
            espacio.actualizarEstado(f_id_espacio)

        else:
            vehiculo = ModelVehiculo()
            vehiculo.set_placa(f_placa)
            vehiculo.set_color(f_color)
            vehiculo.set_tipo_vehiculo(int(f_id_tipo_vehiculo))
            id_new_vehiculo = vehiculo.agregarVehiculoRegistro()

            registro_entrada = ModelRegistroParqueo()
            registro_entrada.set_entrada(format(datetime.now()))
            new_id_registro = registro_entrada.registrarEntrada(f_id_usuario, id_new_vehiculo, f_id_espacio)

            espacio = ModelEspacio()
            espacio.set_estado("OCUPADO")
            espacio.actualizarEstado(f_id_espacio)

        data={'new_id_registro':new_id_registro}
        return JsonResponse(data)

class ImprimirTicket(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        template = get_template('reportes/templete_tickets_entrada.html')

        registro_parqueo = ModelRegistroParqueo()
        datos_registro = registro_parqueo.obtenerDatosParaTicket(kwargs['rpk'])

        context = {"datos_registro": datos_registro}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ticket_entrada.pdf"'

        pisStatus = pisa.CreatePDF(
            html, dest=response
        )
        if pisStatus.err:
            return HttpResponse("OCURRIO UN ERROR")
        return response