from db.models import dictfetchall, TarifaAlquiler
from sistemaparqueo.models.ModelTarifa import ModelTarifa
from django.db import connection

class ModelTarifaAlquiler(ModelTarifa):
    def __init__(self):
        self.__mes=None

    def set_mes(self,mes):
        self.__mes=mes
    def get_mes(self):
        return self.__mes

    def agregar_tarifa_alquiler(self):
        TarifaAlquiler.objects.create(
            meses=self.get_mes(),
            precio=self.get_monto()
        )

    def listar_tarifa_alquiler(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_tarifa_alquiler as id, a.meses as meses, a.precio as precio
        from tarifa_alquiler a
        group by (meses)
                ''')
        total = dictfetchall(cursor)
        return total

    def buscarTarifaAlquilerPorId(self,tarifaAlquilerId):
        return TarifaAlquiler.objects.get(
            id_tarifa_alquiler=tarifaAlquilerId
        )

    def actualizarTarifaAlquiler(self,tarifaAlquilerId):
        tarifa = TarifaAlquiler.objects.get(
            id_tarifa_alquiler=tarifaAlquilerId
        )
        tarifa.meses = self.get_mes()
        tarifa.precio = self.get_monto()
        tarifa.save()


