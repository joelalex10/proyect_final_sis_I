from db.models import dictfetchall, Cliente
from django.db import connection

class ModelCliente():
    def __init__(self):
        self.__ci=None
        self.__nombre=None

    def set_ci(self,ci):
        self.__ci=ci
    def get_ci(self):
        return self.__ci

    def set_nombre(self,nombre):
        self.__nombre=nombre
    def get_nombre(self):
        return self.__nombre

    def buscarClientePorCi(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_cliente, a.nombre
        from cliente a
        where a.ci=%r
        '''%(self.get_ci()))
        total = dictfetchall(cursor)
        if (total):
            return total[0]
        else:
            return {}

    def agregarCliente(self):
        new_cliente=Cliente.objects.create(
            ci=self.get_ci(),
            nombre=self.get_nombre()
        )
        return new_cliente.id_cliente

