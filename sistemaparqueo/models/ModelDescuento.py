from db.models import dictfetchall, Descuento, RegistroParqueo
from django.db import connection

class ModelDescuento():
    def __init__(self):
        self.__monto=None
        self.__descripcion=None

    def set_monto(self,monto):
        self.__monto=monto
    def get_monto(self):
        return self.__monto

    def set_descripcion(self,descripcion):
        self.__descripcion=descripcion
    def get_descripcion(self):
        return self.__descripcion

    def registrarDescuentos(self,parqueoId):
        Descuento.objects.create(
            descripcion=self.get_descripcion(),
            monto=self.get_monto(),
            id_registro_parqueo=RegistroParqueo.objects.get(
                id_parqueo=parqueoId
            )
        )

    def listarDescuentos(self, idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
        select b.id_parqueo, a.monto, a.descripcion
        from descuento a, registro_parqueo b
        where a.id_registro_parqueo = b.id_parqueo
        and b.id_parqueo=%r
        ''' % (idRegistro))

        total = dictfetchall(cursor)
        return total

    def buscarDescuentoPorRegistro(self,idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
        select sum(a.monto) as monto
        from descuento a, registro_parqueo b
        where a.id_registro_parqueo=b.id_parqueo
        and b.id_parqueo=%r
        ''' % (idRegistro))
        total = dictfetchall(cursor)
        return total

    def isDescuento(self,idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
        select *
        from registro_parqueo a, descuento b
        where a.id_parqueo=b.id_registro_parqueo
        and a.id_parqueo=%r
        ''' % (idRegistro))
        total = dictfetchall(cursor)

        if(total):
            return True
        else:
            return False



