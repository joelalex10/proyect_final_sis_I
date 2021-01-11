from django.db import connection

from db.models import dictfetchall, Espacio


class ModelEspacio():
    def __init__(self):
        self.__posicion = None
        self.__estado = None
        self.__sector = None
        self.__tipo_espacio = None

    def set_tipo_espacio(self,tipo_espacio):
        self.__tipo_espacio=tipo_espacio
    def get_tipo_espacio(self):
        return self.__tipo_espacio

    def set_estado(self,estado):
        self.__estado=estado
    def get_estado(self):
        return self.__estado

    def listarEspacios(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_espacio as id, b.tipo as tipo, c.sector as sector,
        a.posicion as posicion, a.estado as estado, b.id_tipo_espacio
        from espacio a, tipo_espacio b, sector c
        where a.id_sector=c.id_sector
        and a.tipo_espacio_id_tipo_espacio=b.id_tipo_espacio
        and a.estado='DISPONIBLE'
        ''')
        total = dictfetchall(cursor)
        return total
    def buscar_espacio_por_Id(self, espacio_id):
        espacio = Espacio.objects.get(
            id_espacio = espacio_id
        )
        return espacio

    def actualizarEstado(self,espacio_id):
        espacio = Espacio.objects.get(
            id_espacio=espacio_id
        )
        espacio.estado=self.get_estado()
        espacio.save()




