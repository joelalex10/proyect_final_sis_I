from db.models import RegistroParqueo, Usuario, Vehiculo, Espacio, dictfetchall, Descuento, Tarifa, RegistroCaja, \
    Incidentes
from django.db import connection


class ModelRegistroParqueo():
    def __init__(self):
        self.__entrada=None
        self.__salida=None

    def set_entrada(self,entrada):
        self.__entrada=entrada
    def get_entrada(self):
        return self.__entrada

    def set_salida(self,salida):
        self.__salida=salida
    def get_salida(self):
        return self.__salida

    def registrarEntrada(self, usuarioId, vehiculoId,espacioId):
        new_registro = RegistroParqueo.objects.create(
            entrada=self.get_entrada(),
            id_usuario=Usuario.objects.get(
                id_usuario= usuarioId
            ),
            vehiculo = Vehiculo.objects.get(
                id_vehiculo = vehiculoId
            ),
            id_espacio=Espacio.objects.get(
                id_espacio = espacioId
            )
        )
        return new_registro.id_parqueo

    def listarVehiculosConEntradaRegistradaPorPlaca(self,placa):
        cursor = connection.cursor()
        cursor.execute('''
                select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
                b.placa as placa, a.entrada as entrada, c.tipo as tipo
                from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
                where a.vehiculo_id=b.id_vehiculo
                and b.tipo_vehiculo_id=c.id_tipo_vehiculo
                and d.id_espacio=a.id_espacio
                and d.id_sector=e.id_sector
                and a.salida is null
                and b.placa=%r
                        '''%(placa))
        total = dictfetchall(cursor)
        return total

    def listarVehiculosConEntradaRegistrada(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
        b.placa as placa, a.entrada as entrada, c.tipo as tipo
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.salida is null
                ''')
        total = dictfetchall(cursor)
        return total

    def listarIncidentesporIdRegistro(self, idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
        select
        a.id_incidentes as id, a.descripcion
        from incidentes a
        where
        a.id_registro_parqueo = %r
        '''%(idRegistro))
        total = dictfetchall(cursor)
        return total

    def registrarIncidentes(self, idRegistro, descripcion_p):
        Incidentes.objects.create(
            descripcion=descripcion_p,
            id_registro_parqueo=RegistroParqueo.objects.get(
                id_parqueo=idRegistro
            )
        )


    def listarVehiculosConSalidaRegistrada(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
        b.placa as placa, a.entrada as entrada, a.salida as salida
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.salida is not null
        order by (a.salida) desc
        ''')
        total = dictfetchall(cursor)
        return total

    def listarVehiculosConSalidaRegistradaPorFechaYPlaca(self,fecha,placa):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
        b.placa as placa, a.entrada as entrada, a.salida as salida
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.entrada between '%s 00:00:00' and '%s 23:59:59'
        and b.placa=%r
        and a.salida is not null
        order by (a.salida) desc
        '''%(fecha,fecha,placa))
        total = dictfetchall(cursor)
        return total

    def listarVehiculosConSalidaRegistradaPorFecha(self,fecha):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
        b.placa as placa, a.entrada as entrada, a.salida as salida
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.entrada between '%s 00:00:00' and '%s 23:59:59'
        and a.salida is not null
        order by (a.salida) desc
        '''%(fecha,fecha))
        total = dictfetchall(cursor)
        return total

    def listarVehiculosConSalidaRegistradaPorPlaca(self, placa):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, e.sector as sector, d.posicion as posicion,
        b.placa as placa, a.entrada as entrada, a.salida as salida
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and b.placa=%r
        and a.salida is not null
        order by (a.salida) desc
        ''' % (placa))
        total = dictfetchall(cursor)
        return total

    def buscarRegistroPorId(self,registroParqueoId):
        cursor = connection.cursor()
        cursor.execute('''
        select *
        from registro_parqueo a
        where a.id_parqueo=%r'''%(registroParqueoId))
        total = dictfetchall(cursor)
        return total[0]

    def buscarRegistroEntradasPorDetalles(self,entrada,salida,sector,posicion):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, b.placa as placa, a.entrada as entrada, a.salida as salida,
        c.tipo as tipo, b.color, e.sector, d.posicion
        from registro_parqueo a, vehiculo b, tipo_vehiculo c,
        espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.salida is not null
        and a.entrada between %r and %r
        and e.sector=%r
        and d.posicion=%r
        '''%(entrada,salida,sector,posicion))
        total = dictfetchall(cursor)
        return total

    def buscarRegistroSalidasPorDetalles(self,entrada,salida,sector,posicion):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo as id, b.placa as placa, a.entrada as entrada, a.salida as salida,
        c.tipo as tipo, b.color, e.sector, d.posicion
        from registro_parqueo a, vehiculo b, tipo_vehiculo c,
        espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.salida is not null
        and a.salida between %r and %r
        and e.sector=%r
        and d.posicion=%r
        '''%(entrada,salida,sector,posicion))
        total = dictfetchall(cursor)
        return total

    def obtenerDatosParaTicket(self,idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
                select d.posicion, e.sector, a.entrada, a.salida, b.placa, b.color, a.id_tarifas
                from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
                where a.vehiculo_id=b.id_vehiculo
                and b.tipo_vehiculo_id=c.id_tipo_vehiculo
                and d.id_espacio=a.id_espacio
                and d.id_sector=e.id_sector
                and a.id_parqueo=%r
                ''' % (idRegistro))
        total = dictfetchall(cursor)
        if (total):
            return total[0]
        else:
            return False



    def buscarRegistroPorIdParaHistorial(self, idRegistro):
        cursor = connection.cursor()
        cursor.execute('''
        select d.posicion, e.sector, a.entrada, a.salida, b.placa
        from registro_parqueo a, vehiculo b, tipo_vehiculo c, espacio d, sector e
        where a.vehiculo_id=b.id_vehiculo
        and b.tipo_vehiculo_id=c.id_tipo_vehiculo
        and d.id_espacio=a.id_espacio
        and d.id_sector=e.id_sector
        and a.salida is not null
        and a.id_parqueo=%r
        '''%(idRegistro))
        total = dictfetchall(cursor)

        if(total):
            return total[0]
        else:
            return False




    def registrarSalida(self, registroId, tarifaId, precio_total):

        registro= RegistroParqueo.objects.get(
            id_parqueo=registroId,
        )
        registro.salida=self.get_salida()
        registro.id_tarifas=Tarifa.objects.get(id_tarifas = tarifaId)
        registro.save()

        caja = RegistroCaja.objects.get(
            estado='ACTIVO'
        )
        pg=Tarifa.objects.get(id_tarifas = tarifaId)

        caja.monto_facturado = caja.monto_facturado + precio_total
        caja.save()

    def registrarSalidaAlquiler(self, registroId):
        registro= RegistroParqueo.objects.get(
            id_parqueo=registroId,
        )
        registro.salida=self.get_salida()
        registro.save()


    def obtenerHorasYDiasParqueo(self, fechaInicio, fechaSalida):
        cursor = connection.cursor()
        cursor.execute('''
        SELECT TIMESTAMPDIFF(DAY, %r, %r) as dias
        '''%(fechaInicio,fechaSalida))
        total = dictfetchall(cursor)

        cursor.execute('''
        SELECT MOD(TIMESTAMPDIFF(HOUR, %r, %r), 24) +1 as horas
        ''' % (fechaInicio, fechaSalida))
        total1 = dictfetchall(cursor)

        horas=total1[0]['horas']
        dias=total[0]['dias']
        if(horas>23):
            horas=0
            dias=dias+1
        return {"horas":horas, "dias":dias}

    def verificarEstadoAlquilerVehiculo(self, registroId):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_parqueo, b.cliente_id
        from registro_parqueo a, vehiculo b, alquiler c
        where a.vehiculo_id=b.id_vehiculo
        and b.id_vehiculo=c.vehiculo_id_vehiculo
        and c.estado='ACTIVO'
        and a.id_parqueo=%r
        '''%(registroId))
        total = dictfetchall(cursor)

        if(total):
            return True
        else:
            return False






