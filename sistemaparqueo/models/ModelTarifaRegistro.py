from db.models import dictfetchall, Tarifa
from sistemaparqueo.models.ModelTarifa import ModelTarifa
from django.db import connection

class ModelTarifaRegistro(ModelTarifa):

    def __init__(self):
        self.__hora=None
        self.__dia=None

    def set_hora(self,hora):
        self.__hora=hora
    def get_hora(self):
        return self.__hora

    def set_dia(self,dia):
        self.__dia=dia
    def get_dia(self):
        return self.__dia

    def agregar_tarifa_registro(self):
        Tarifa.objects.create(
            horas=self.get_hora(),
            dias=self.get_dia(),
            precio=self.get_monto()
        )

    def listar_tarifas_registro(self):

        cursor = connection.cursor()
        cursor.execute('''
        select a.id_tarifas as id, a.horas as horas, 
        a.dias as dias, a.precio as precio
        from tarifa a
        
        ''')
        total = dictfetchall(cursor)
        return total

    def buscarTarifaPorId(self, tarifaRegistroId):
        return Tarifa.objects.get(
            id_tarifas=tarifaRegistroId
        )

    def actualizarTarifaRegistro(self, tarifaId):
        tarifa = Tarifa.objects.get(
            id_tarifas =tarifaId
        )
        tarifa.horas=self.get_hora()
        tarifa.dias=self.get_dia()
        tarifa.precio=self.get_monto()
        tarifa.save()

    def buscarTarifaPorFechaYHora(self,diasP,horaP):
        tarifa = Tarifa.objects.get(
            horas=horaP,
            dias=diasP
        )
        return tarifa