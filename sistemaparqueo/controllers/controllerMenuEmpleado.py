from django.http import JsonResponse
from django.views.generic import TemplateView,ListView
from django.views import View

from sistemaparqueo.models.ModelAlquiler import ModelAlquiler
from sistemaparqueo.models.ModelCaja import ModelCaja
from sistemaparqueo.models.ModelEspacio import ModelEspacio
from sistemaparqueo.models.ModelRegistroParqueo import ModelRegistroParqueo
from sistemaparqueo.models.ModelUsuario import ModelUsuario
from sistemaparqueo.models.ModelVehiculo import ModelVehiculo


class MostrarControlDeAlquileres(TemplateView):
    template_name = 'viewAlquileres.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarControlDeAlquileres, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        alquiler=ModelAlquiler()
        context["lista_alquileres"]=alquiler.listar_Alquileres()
        return context

class MostrarIngresoVehiculos(TemplateView):
    template_name = 'viewIngresoVehiculos/viewIngresoVehiculo.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarIngresoVehiculos, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        vehiculo = ModelVehiculo()
        context["tipo_vehiculos"] = vehiculo.listar_tipo_vehiculos()

        espacio = ModelEspacio()
        context['lista_espacios'] = espacio.listarEspacios()

        return context

class MostrarSalidaVehiculos(TemplateView):
    template_name = 'viewSalidaVehiculos/viewSalidaVehiculo.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarSalidaVehiculos, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        registro_parqueo=ModelRegistroParqueo()
        lista_entradas=registro_parqueo.listarVehiculosConEntradaRegistrada()
        context["registro_entradas"]=lista_entradas

        return context


class MostrarAperturaCaja(TemplateView):
    template_name = 'viewAperturaCaja/viewAperturaCaja.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarAperturaCaja, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        return context

class MostrarCierreCaja(TemplateView):
    template_name = 'viewCierreCaja/viewCierreCaja.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarCierreCaja, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)


        caja = ModelCaja()
        caja.set_estado('ACTIVO')
        estado = caja.verificarEstadoCaja()
        context["datos_apertura"] = estado[0]


        return context

class VerificarAperturaDeCaja(View):
    def get(self,request):
        caja = ModelCaja()
        caja.set_estado('ACTIVO')
        estado= caja.verificarEstadoCaja()
        if(estado):
            data = {"estado":estado}
        else:
            data = {}
        return JsonResponse(data)

class VerificarCierreDeCaja(View):
    def get(self,request):
        caja = ModelCaja()
        caja.set_estado('ACTIVO')
        estado= caja.verificarEstadoCaja()
        if(estado):
            data = {}
        else:
            data = {"estado":estado}
        return JsonResponse(data)





