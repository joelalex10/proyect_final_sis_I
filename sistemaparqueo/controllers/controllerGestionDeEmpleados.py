from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from sistemaparqueo.models.ModelEmpleado import ModelEmpleado
from sistemaparqueo.models.ModelUsuario import ModelUsuario


class AgregarEmpleado(View):

    def get(self,request):
        f_ci=request.GET.get("ci")
        f_nombre=request.GET.get("nombre")
        f_usuario = request.GET.get("usuario")
        f_password = request.GET.get("password")
        f_horaIngreso = request.GET.get("horaIngreso")
        f_horaSalida = request.GET.get("horaSalida")

        empleado = ModelEmpleado()
        empleado.set_ci(f_ci)
        empleado.set_nombre(f_nombre)
        empleado.set_nombre_usuario(f_usuario)
        empleado.set_password(f_password)
        empleado.set_hora_ingreso(f_horaIngreso)
        empleado.set_hora_salida(f_horaSalida)
        empleado.agregarEmpleado()

        data = {}
        return JsonResponse(data)

class MostrarModalEdicion(TemplateView):
    template_name = 'viewGestionDeEmpleados/modalEditEmpleado.html'
    def get_context_data(self, **kwargs):
        context = super(MostrarModalEdicion, self).get_context_data(**kwargs)
        print("EL ID ES:")
        print(kwargs['pk'])
        obj = ModelUsuario()
        context["usuario"] = obj.buscarUsuarioPorId(kwargs['pk'])
        return context

class EditarEmpleado(View):
    def get(self,request):
        f_id = request.GET.get("id")
        f_ci = request.GET.get("ci")
        f_nombre = request.GET.get("nombre")
        f_usuario = request.GET.get("usuario")
        f_password = request.GET.get("password")
        f_horaIngreso = request.GET.get("horaIngreso")
        f_horaSalida = request.GET.get("horaSalida")

        empleado = ModelEmpleado()
        empleado.set_ci(f_ci)
        empleado.set_nombre(f_nombre)
        empleado.set_nombre_usuario(f_usuario)
        empleado.set_password(f_password)
        empleado.set_hora_ingreso(f_horaIngreso)
        empleado.set_hora_salida(f_horaSalida)
        print("LOS HORARIOS SON")
        print(f_horaIngreso)
        print(f_horaSalida)
        empleado.editarEmpleado(f_id)
        data={"datos":f_id}
        return JsonResponse(data)

