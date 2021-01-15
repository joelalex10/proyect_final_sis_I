from django.db import connection
from db.models import TipoUsuario, Usuario


class ModelUsuario:
    def __init__(self,):
        self.__ci=None
        self.__nombre=None
        self.__telefono=None
        self.__password=None
        self.__nombre_usuario=None
        self.__tipo_usuario=None

    def set_tipo_usuario(self,tipo_usuario):
        self.__tipo_usuario=tipo_usuario
    def get_tipo_usuario(self):
        return self.__tipo_usuario

    def set_ci(self,ci):
        self.__ci = ci
    def get_ci(self):
        return self.__ci

    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_telefono(self,telefono):
        self.__telefono = telefono
    def get_telefono(self):
        return self.__telefono

    def set_password(self,password):
        self.__password = password
    def get_password(self):
        return self.__password

    def set_nombre_usuario(self,nombre_usuario):
        self.__nombre_usuario = nombre_usuario
    def get_nombre_usuario(self):
        return self.__nombre_usuario

    def mostrarListaTipoUsuario(self):
        tipo_usuarios = TipoUsuario.objects.all()
        return tipo_usuarios

    def consultarUsuario(self,):
        list_id_usuario=Usuario.objects.filter(usuario = self.__nombre_usuario,
          password = self.__password,
          id_tipo_usuario= TipoUsuario.objects.get(
              id_tipo_usuario=self.__tipo_usuario
          ))
        if(list_id_usuario.exists()):
            return list_id_usuario[0]
        else:
            return False

    def buscarUsuarioPorId(self,usuarioId):
        return Usuario.objects.get(id_usuario=usuarioId)


