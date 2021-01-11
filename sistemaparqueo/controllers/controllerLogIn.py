from django.shortcuts import render, redirect
from django.db import connection

from django.views.generic import TemplateView,ListView

from sistemaparqueo.models.ModelUsuario import ModelUsuario


class MostrarInicio(TemplateView):
    template_name = 'viewLogIn.html'

    def get_context_data(self, **kwargs):
        context = super(MostrarInicio,self).get_context_data(**kwargs)
        usuario = ModelUsuario()
        tipo_usuarios = usuario.mostrarListaTipoUsuario()
        context["tipo_usuarios"]=tipo_usuarios
        return context

    def post(self, request):
        f_nombre_usuario = request.POST.get('user_name')
        f_contrasena = request.POST.get('password')
        f_tipo_usuario = request.POST.get('user_type')

        usuario = ModelUsuario()
        usuario.set_nombre_usuario(f_nombre_usuario)
        usuario.set_password(f_contrasena)
        usuario.set_tipo_usuario(f_tipo_usuario)

        respuesta = usuario.consultarUsuario()

        if (f_tipo_usuario=='1' and respuesta!=0):
            return redirect('menuAdmin',int(respuesta.id_usuario))
        elif (f_tipo_usuario=='2' and respuesta!=0):
            return redirect('menuEmpleado',int(respuesta.id_usuario))

        return redirect('index')

class MostrarMenuAdmin(TemplateView):
    template_name = 'viewMenuPrincipal.html'


    def get_context_data(self, **kwargs):
        context = super(MostrarMenuAdmin, self).get_context_data(**kwargs)
        id_usuario = kwargs['pk']
        usuario = ModelUsuario()
        context["usuario"] = usuario.buscarUsuarioPorId(id_usuario)
        return context

class MostrarMenuEmpleado(TemplateView):
    template_name = 'viewMenuEmpleado.html'
    def get_context_data(self, *args, **kwargs):
        context = super(MostrarMenuEmpleado, self).get_context_data(**kwargs)
        id_usuario=kwargs['pk']
        usuario=ModelUsuario()
        context["usuario"]=usuario.buscarUsuarioPorId(id_usuario)
        return context


