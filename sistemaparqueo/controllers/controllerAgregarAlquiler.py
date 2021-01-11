from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from sistemaparqueo.models.ModelAdministrador import ModelAdministrador
from sistemaparqueo.models.ModelAlquiler import ModelAlquiler
from sistemaparqueo.models.ModelCliente import ModelCliente
from sistemaparqueo.models.ModelTarifaAlquiler import ModelTarifaAlquiler
from sistemaparqueo.models.ModelVehiculo import ModelVehiculo
from datetime import datetime

class BuscarCiCliente(View):
    def get(self,request):
        f_ci = request.GET.get('ci')
        print(f_ci)
        cliente = ModelCliente()
        cliente.set_ci(f_ci)
        variable = cliente.buscarClientePorCi()
        if(variable=={}):
            data = {}
        else:
            data = {"cliente": variable}
        return JsonResponse(data)

class BuscarVehiculoPlaca(View):
    def get(self, request):
        f_placa = request.GET.get('placa')
        f_id_cliente=request.GET.get('idCliente')
        print("EL ID CLIENTE ES: ")
        print(f_id_cliente)
        vehiculo=ModelVehiculo()
        vehiculo.set_placa(f_placa)
        variable=vehiculo.buscarVehiculoPorPlaca(f_id_cliente)

        if (variable == {}):
            data = {}
        else:
            data = {"vehiculo": variable}
        return JsonResponse(data)

class AgregarAlquiler(View):
    def get(self, request):
        f_id_cliente=request.GET.get('idCliente')
        f_id_Vehiculo=request.GET.get('idVehiculo')

        f_ci = request.GET.get('ci')
        f_nombre = request.GET.get('nombre')
        f_placa = request.GET.get('placa')
        f_marca_modelo = request.GET.get('marcaModelo')
        f_color = request.GET.get('color')
        f_tipoVehiculo = request.GET.get('tipoVehiculo')
        f_tarifa = request.GET.get('tarifa')
        f_numCuotas = request.GET.get('numCuotas')


        tarifa_alquiler=ModelTarifaAlquiler()
        tarifa_obj = tarifa_alquiler.buscarTarifaAlquilerPorId(f_tarifa)
        print("LOS MESES DE LA TARIFA SON:")
        print(tarifa_obj.meses)
        print("LA FECHA INICIO ES: ")


        if (f_id_cliente == '0' and f_id_Vehiculo == '0'):
            print ("cliente y vehiculo nuevo")

            new_cliente = ModelCliente()
            new_cliente.set_ci(f_ci)
            new_cliente.set_nombre(f_nombre)
            new_id_cliente = new_cliente.agregarCliente()

            new_vehiculo = ModelVehiculo()
            new_vehiculo.set_placa(f_placa)
            new_vehiculo.set_marca_modelo(f_marca_modelo)
            new_vehiculo.set_color(f_color)
            new_vehiculo.set_tipo_vehiculo(f_tipoVehiculo)
            new_id_vehiculo = new_vehiculo.agregarVehiculo(new_id_cliente)

            new_alquiler = ModelAlquiler()
            new_alquiler.set_inicio(datetime.now().strftime("%Y-%m-%d"))
            new_alquiler.set_fin(new_alquiler.definirFinAlquiler(tarifa_obj.meses)['fin'])
            new_alquiler.set_estado("ACTIVO")
            new_alquiler.set_cuotas(int(f_numCuotas))
            new_alquiler.definirCuotas()
            new_alquiler.agregar_alquiler(new_id_cliente, new_id_vehiculo, tarifa_obj)



        elif(f_id_Vehiculo == '0'):

            new_vehiculo = ModelVehiculo()
            new_vehiculo.set_placa(f_placa)
            new_vehiculo.set_marca_modelo(f_marca_modelo)
            new_vehiculo.set_color(f_color)
            new_vehiculo.set_tipo_vehiculo(f_tipoVehiculo)
            new_id_vehiculo = new_vehiculo.agregarVehiculo(f_id_cliente)

            new_alquiler = ModelAlquiler()
            new_alquiler.set_inicio(datetime.now().strftime("%Y-%m-%d"))
            new_alquiler.set_fin(new_alquiler.definirFinAlquiler(tarifa_obj.meses)['fin'])
            new_alquiler.set_estado("ACTIVO")
            new_alquiler.set_cuotas(int(f_numCuotas))
            new_alquiler.definirCuotas()
            new_alquiler.agregar_alquiler(f_id_cliente, new_id_vehiculo, tarifa_obj)




        else:

            new_alquiler = ModelAlquiler()
            new_alquiler.set_inicio(datetime.now().strftime("%Y-%m-%d"))
            new_alquiler.set_fin(new_alquiler.definirFinAlquiler(tarifa_obj.meses)['fin'])
            new_alquiler.set_estado("ACTIVO")
            new_alquiler.set_cuotas(int(f_numCuotas))
            new_alquiler.definirCuotas()
            new_alquiler.agregar_alquiler(f_id_cliente, f_id_Vehiculo, tarifa_obj)

            print("vehiculo y cliente registrados")

        data={}
        return JsonResponse(data)
