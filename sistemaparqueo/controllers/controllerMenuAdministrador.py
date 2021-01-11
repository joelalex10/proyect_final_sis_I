
from django.views.generic import TemplateView,ListView

from sistemaparqueo.models.ModelAlquiler import ModelAlquiler
from sistemaparqueo.models.ModelEmpleado import ModelEmpleado
from sistemaparqueo.models.ModelRegistroParqueo import ModelRegistroParqueo
from sistemaparqueo.models.ModelTarifaAlquiler import ModelTarifaAlquiler
from sistemaparqueo.models.ModelTarifaRegistro import ModelTarifaRegistro
from sistemaparqueo.models.ModelUsuario import ModelUsuario
from sistemaparqueo.models.ModelAdministrador import ModelAdministrador


class MostrarReporteCaja(TemplateView):
    template_name = 'viewReporteCaja.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarReporteCaja, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        adm=ModelAdministrador()
        lista_registro=adm.mostrarReporteCaja()
        context["listado_caja"]=lista_registro

        lista_total_registro=adm.mostrarTotalReporteCaja()
        context["suma_caja"]=lista_total_registro

        return context



class MostrarGestionEmpleados(TemplateView):
    template_name = 'viewGestionDeEmpleados/contentGestionDeEmpleados.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarGestionEmpleados, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        emp=ModelEmpleado()
        lista=emp.listaEmpleados()
        context["empleados"] = lista
        return context

class MostrarGestionTarifas(TemplateView):
    template_name = 'viewGestionDeTarifas/contentGestionDeTarifas.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarGestionTarifas, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        tarifa_registro = ModelTarifaRegistro()
        list_tarifa_registro = tarifa_registro.listar_tarifas_registro()
        context["lista_tarifas_registro"] = list_tarifa_registro

        tarifa_alquiler = ModelTarifaAlquiler()
        list_tarifa_alquiler = tarifa_alquiler.listar_tarifa_alquiler()
        context["lista_tarifas_alquiler"] = list_tarifa_alquiler

        return context

class MostrarReporteDeAlquileres(TemplateView):
    template_name = 'viewReporteAlquileres/contentReporteDeAlquileres.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarReporteDeAlquileres, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        alquiler = ModelAlquiler()
        context["lista_alquileres"] = alquiler.listar_Alquileres()

        return context

class MostrarControlEmpleados(TemplateView):
    template_name = 'viewControlPersonal.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarControlEmpleados, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)
        empleado = ModelEmpleado()
        context["lista_horas"] = empleado.listarEntradaDeEmpleados()
        return context

class MostrarHistorialUbicacion(TemplateView):
    template_name = 'viewHistorialUbicacion/viewHistorialUbicacion.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarHistorialUbicacion, self).get_context_data(**kwargs)

        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)

        registros = ModelRegistroParqueo()
        lista = registros.listarVehiculosConSalidaRegistrada()
        context["lista_salidas"]=lista


        return context



