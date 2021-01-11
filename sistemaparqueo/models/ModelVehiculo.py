from db.models import dictfetchall, Vehiculo, TipoVehiculo, Cliente
from django.db import connection

class ModelVehiculo():
    def __init__(self):
        self.__placa=None
        self.__marca_modelo=None
        self.__color=None
        self.__tipo_vehiculo=None

    def set_placa(self,placa):
        self.__placa=placa
    def get_placa(self):
        return self.__placa

    def set_marca_modelo(self,marca_modelo):
        self.__marca_modelo=marca_modelo
    def get_marca_model(self):
        return self.__marca_modelo

    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color

    def set_tipo_vehiculo(self,tipo_vehiculo):
        self.__tipo_vehiculo=tipo_vehiculo
    def get_tipo_vehiculo(self):
        return self.__tipo_vehiculo

    def agregarVehiculo(self,clienteId):
        new_vehicle = Vehiculo.objects.create(
            placa = self.get_placa(),
            marca_modelo = self.get_marca_model(),
            color = self.get_color(),
            cliente = Cliente.objects.get(
                id_cliente=clienteId
            ),
            tipo_vehiculo = TipoVehiculo.objects.get(
                id_tipo_vehiculo = self.get_tipo_vehiculo()
            )
        )
        return new_vehicle.id_vehiculo

    def buscarVehiculoPorPlaca(self,cliente_id):
        cursor = connection.cursor()
        cursor.execute('''
            select a.id_vehiculo, a.marca_modelo, a.color,
            a.tipo_vehiculo_id, a.placa
            from vehiculo a
            where a.placa=%r
            and a.cliente_id=%r
                ''' % (self.get_placa(),cliente_id))
        total = dictfetchall(cursor)
        if (total):
            return total[0]
        else:
            return {}

    def listar_tipo_vehiculos(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_tipo_vehiculo as id, a.tipo as tipo
        from tipo_vehiculo a
        ''')
        total = dictfetchall(cursor)
        return total

    def buscarVehiculoPorPlaca_only(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_vehiculo, a.marca_modelo, a.color,
        a.tipo_vehiculo_id, a.placa
        from vehiculo a
        where a.placa=%r
        '''%(self.get_placa()))
        total = dictfetchall(cursor)
        return total

    def agregarVehiculoRegistro(self):
        new_vehiculo =Vehiculo.objects.create(
            placa = self.get_placa(),
            color=self.get_color(),
            tipo_vehiculo=TipoVehiculo.objects.get(
                id_tipo_vehiculo = self.get_tipo_vehiculo()
            )
        )
        return new_vehiculo.id_vehiculo


