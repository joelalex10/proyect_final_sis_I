"""sistemaparqueo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add viewGestionDeEmpleados URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add viewGestionDeEmpleados URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add viewGestionDeEmpleados URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from sistemaparqueo.controllers import controllerLogIn, controllerMenuAdministrador, controllerReporteCaja, \
    controllerGestionDeEmpleados, controllerGestionDeTarifas, controllerMenuEmpleado, controllerControlAlquileres, \
    controllerReporteAlquileres, controllerAgregarAlquiler, controllerIngresoVehiculos, controllerSalidaVehiculos, \
    controllerAperturaCaja, controllerCierreCaja, controllerControlPersonal, controllerEstadoPagos, \
    controllerHistorialUbicacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',controllerLogIn.MostrarInicio.as_view(), name='index'),
    path('<int:pk>/menuPrincipal/',controllerLogIn.MostrarMenuAdmin.as_view(), name='menuAdmin'),
    path('<int:pk>/menuEmpleado/', controllerLogIn.MostrarMenuEmpleado.as_view(), name='menuEmpleado'),

    path('<int:pk>/menuPrincipal/reporteCaja/', controllerMenuAdministrador.MostrarReporteCaja.as_view(), name ='reporteCaja'),
    path('<int:pk>/menuPrincipal/gestionEmpleados/',controllerMenuAdministrador.MostrarGestionEmpleados.as_view(), name='gestionUsuarios'),
    path('<int:pk>/menuPrincipal/gestionDeTarifas/',controllerMenuAdministrador.MostrarGestionTarifas.as_view(), name='gestionTarifas'),
    path('<int:pk>/menuPrincipal/reporteAlquileres/',controllerMenuAdministrador.MostrarReporteDeAlquileres.as_view(), name='reporteAlquileres'),
    path('<int:pk>/menuPrincipal/controlEmpleados/',controllerMenuAdministrador.MostrarControlEmpleados.as_view(), name='controlEmpleados'),
    path('<int:pk>/menuPrincipal/historialUbicacion/',controllerMenuAdministrador.MostrarHistorialUbicacion.as_view(), name='historial_ubicacion'),

    path('<int:pk>/menuEmpleado/controlAlquileres/',controllerMenuEmpleado.MostrarControlDeAlquileres.as_view(),name='controlAlquileres'),
    path('<int:pk>/menuEmpleado/ingresoVehiculos/',controllerMenuEmpleado.MostrarIngresoVehiculos.as_view(), name='ingresoVehiculos'),
    path('<int:pk>/menuEmpleado/AperturaCaja/',controllerMenuEmpleado.MostrarAperturaCaja.as_view(), name='apertura_caja'),
    path('<int:pk>/menuEmpleado/SalidaVehiculos/',controllerMenuEmpleado.MostrarSalidaVehiculos.as_view(), name='salida_de_vehiculos'),
    path('<int:pk>/menuEmpleado/CierreCaja/',controllerMenuEmpleado.MostrarCierreCaja.as_view(), name='cierre_caja'),

    path('menuEmpleado/verificarEstadoCaja/',controllerMenuEmpleado.VerificarAperturaDeCaja.as_view(), name='verificar_apertura_caja'),
    path('menuEmpleado/verificarCierreCaja/',controllerMenuEmpleado.VerificarCierreDeCaja.as_view(), name='verificar_cierre_caja'),

    path('<int:pk>/menuEmpleado/controlAlquileres/<int:ak>',controllerControlAlquileres.MostrarEstadoPagos.as_view(), name='estadoPagos'),
    path('<int:pk>/menuEmpleado/controlAlquileres/agregarAlquiler',controllerControlAlquileres.MostrarAgregarAlquiler.as_view(), name='agregarAlquiler'),
    path('menuEmpleado/controlAlquileres/buscarPorFiltros/',controllerControlAlquileres.BuscarAlquilerPorFiltros.as_view(), name='buscar_control_alquiler_por_filtros'),
    path('menuEmpleado/controlAlquileres/agregarAlquiler/buscarCiCliente',controllerAgregarAlquiler.BuscarCiCliente.as_view(), name='buscarCiCliente'),
    path('menuEmpleado/controlAlquileres/agregarAlquiler/buscarPlacaVehiculo',controllerAgregarAlquiler.BuscarVehiculoPlaca.as_view(), name='buscarPlacaVehiculo'),
    path('menuEmpleado/ControlAlquileres/agregarAlquiler/agregarAlquiler',controllerAgregarAlquiler.AgregarAlquiler.as_view(), name='agregarAlquiler'),
    path('menuEmpleado/ControlAlquileres/pagarCuotaAlquiler/',controllerEstadoPagos.PagarCuotas.as_view(), name="pagar_cuotas"),
    path('menuEmpleado/ControlAlquileres/pagarCuotaAlquiler/imprimirFactura/<int:fpk>',controllerEstadoPagos.ImprimirFacturaPagosAlquileres.as_view(), name='imprimir_factura_alquiler'),

    path('menuEmpleado/ingresoVehiculos/buscarVehiculoAlquiler/',controllerIngresoVehiculos.BuscarPlacaAlquiler.as_view(), name='buscar_placa_vehiculo'),
    path('menuEmpleado/ingresoVehiculos/registrarEntrada/',controllerIngresoVehiculos.RegistrarEntrada.as_view(), name='registrar_entrada'),
    path('menuEmpleado/ingresoVehiculos/imprimirTicketEntrada/<int:rpk>',controllerIngresoVehiculos.ImprimirTicket.as_view(), name="ticket"),

    path('menuEmpleado/SalidaVehiculos/buscarPorFiltros/',controllerSalidaVehiculos.BuscarVehiculoPorFiltro.as_view(), name='buscar_salida_filtros'),
    path('menuEmpleado/SalidaVehiculos/verificarEstadoAlquiler/',controllerSalidaVehiculos.VerificarEstadoAlquilerRegistro.as_view(), name='verificar_alquiler'),
    path('menuEmpleado/SalidaVehiculos/mostrar_agregarDescuento/<int:rpk>',controllerSalidaVehiculos.MostrarModalDescuentos.as_view(), name='agregar_descuento'),
    path('menuEmpleado/SalidaVehiculos/registrarDescuento/', controllerSalidaVehiculos.RegistrarDescuento.as_view(), name='registrar_descuento'),
    path('menuEmpleado/SalidaVehiculos/mostrar_agregarIncidente/<int:rpk>',controllerSalidaVehiculos.MostrarModalIncidentes.as_view(), name='agregar_incidente'),
    path('menuEmpleado/SalidaVehiculos/registrarIncidentes/', controllerSalidaVehiculos.RegistrarIncidente.as_view(), name='registrar_incidentes'),
    path('menuEmpleado/SalidaVehiculos/mostrar_registrarSalida/<int:rpk>',controllerSalidaVehiculos.MostrarModalRegistrarSalida.as_view(), name='mostrar_registrar_salida'),
    path('menuEmpleado/SalidaVehiculos/registrar_salida',controllerSalidaVehiculos.RegistrarSalida.as_view(), name='registrar_salida'),
    path('menuEmpleado/SalidaVehiculos/imprimirTicketSalida/<int:rpk>',controllerSalidaVehiculos.ImprimirTicketSalida.as_view(), name='ticket_salida'),

    path('menuEmpleado/AperturaCaja/totalLiteral/',controllerAperturaCaja.CalcularTotal.as_view(), name='calcular_total'),
    path('<int:pk>/menuEmpleado/AperturaCaja/abrirModalConfirmacion/',controllerAperturaCaja.AbrirModalConfirmacion.as_view(), name='abrir_modal_apertura_caja'),
    path('menuEmpleado/AperturaCaja/verificarEstado/',controllerAperturaCaja.VerificarEstadoCaja.as_view(), name='verificar_estado_caja'),
    path('menuEmpleado/AperturaCaja/registrarAperturaCaja/',controllerAperturaCaja.RegistrarApertura.as_view(), name='registrar_apertura'),

    path('<int:pk>/menuEmpleado/CierreCaja/abrirModalConfirmacion',controllerCierreCaja.MostrarModalConfirmacion.as_view(), name='abrir_modal_cierre_caja'),
    path('menuEmpleado/CierreCaja/registrarCierreCaja',controllerCierreCaja.RegistrarClausura.as_view(), name='registrar_clausura'),

    path('menuPrincipal/reporteCaja/filtros',controllerReporteCaja.FiltrosReporteCaja.as_view(), name='filtrar_reporte_caja'),

    path('menuPrincipal/gestionEmpleados/agregarEmpleado',controllerGestionDeEmpleados.AgregarEmpleado.as_view(), name='agregar_empleado'),
    path('menuPrincipal/gestionEmpleados/mostrarEditarEmpleado/<int:pk>',controllerGestionDeEmpleados.MostrarModalEdicion.as_view(), name='mostrar_editar_cliente'),
    path('menuPrincipal/gestionEmpleados/editarEmpleado',controllerGestionDeEmpleados.EditarEmpleado.as_view(), name='editar_cliente'),

    path('menuPrincipal/gestionDeTarifas/agregarTarifa/',controllerGestionDeTarifas.AgregarTarifas.as_view(), name='agregar_tarifa_registro'),
    path('menuPrincipal/gestionDeTarifas/agregarTarifaAlquiler/', controllerGestionDeTarifas.AgregarTarifaAlquiler.as_view(),name='agregar_tarifa_alqiler'),

    path('menuPrincipal/gestionDeTarifas/mostrarEditarTarifa/<int:pk>',controllerGestionDeTarifas.MostrarModalTarifaRegistro.as_view(), name='mostrar_editar_tarifa_registro'),
    path('menuPrincipal/gestionDeTarifas/editarTarifaRegistro/',controllerGestionDeTarifas.EditarTarifaRegistro.as_view(), name='editar_tarifa_registro'),
    path('menuPrincipal/gestionDeTarifas/mostrarEditarTarifaAlquiler/<int:pk>',controllerGestionDeTarifas.MostrarModalTarifaAlquiler.as_view(), name='mostrar_editar_tarifa_alquiler'),
    path('menuPrincipal/gestionDeTarifas/editarTarifaAlquiler/',controllerGestionDeTarifas.EditarTarifaAlquiler.as_view(), name = 'editar_tarifa_alquiler'),

    path('menuPrincipal/reporteAlquileres/<int:ak>',controllerReporteAlquileres.MostrarModalEstadoPagos.as_view(), name='mostrar_estado_pagos'),
    path('menuPrincipal/reporteAlquileres/buscarPorFiltros',controllerReporteAlquileres.BuscarPorFiltros.as_view(), name='buscar_alquiler_por_filtro'),

    path('menuPrincipal/controlEmpleados/buscarPorFiltros',controllerControlPersonal.BuscarPorFiltros.as_view(), name='buscar_filtros_empleados'),

    path('menuPrincipal/historialUbicacion/mostrarModalIncidentes/<int:pki>',controllerHistorialUbicacion.MostrarModalIncidentes.as_view(), name='modal_historial_ubicacion'),
    path('menuPrincipal/historialUbicacion/mostrarModalDescuentos/<int:pki>',controllerHistorialUbicacion.MostrarModalDescuentos.as_view(), name='modal_historial_descuentos'),
    path('menuPrincipal/historialUbicacion/mostrarModalDetalles/<int:pki>',controllerHistorialUbicacion.MostrarDetalles.as_view(), name='modal_historial_detalles'),
    path('menuPrincipal/historialUbicacion/buscarPorFiltros',controllerHistorialUbicacion.BuscarHistorialPorFiltros.as_view(), name='filtros_historial_ubicacion'),
]
