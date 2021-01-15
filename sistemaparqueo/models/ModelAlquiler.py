from datetime import date

from django.db import connection

from db.models import dictfetchall, Alquiler, Cliente, TarifaAlquiler, Vehiculo, PlanPagos, PagosAlquileres, \
    RegistroCaja


class ModelAlquiler():
    def __init__(self):
        self.__inicio=None
        self.__fin=None
        self.__cuotas=None
        self.__estado=None

    def set_inicio(self,inicio):
        self.__inicio=inicio
    def get_inicio(self):
        return self.__inicio

    def set_fin(self,fin):
        self.__fin=fin
    def get_fin(self):
        return self.__fin

    def set_cuotas(self,cuotas):
        self.__cuotas= cuotas
    def get_cuotas(self):
        return self.__cuotas

    def set_estado(self,estado):
        self.__estado=estado
    def get_estado(self):
        return self.__estado

    def definirCuotas(self):
        pass
    def agregar_alquiler(self, clienteId, vehiculoId, tarifa):
        print("LOS DATOS DE ALQUILER SON: ")
        new_alquiler=Alquiler.objects.create(
            inicio = self.get_inicio(),
            fin = self.get_fin(),
            estado = self.get_estado(),
            cliente_id_cliente = Cliente.objects.get(
                id_cliente = clienteId
            ),
            id_tarifa_alquiler = tarifa,
            vehiculo_id_vehiculo = Vehiculo.objects.get(
                id_vehiculo = vehiculoId
            )
        )
        plan_pagos =PlanPagos.objects.create(
            num_cuotas = self.get_cuotas(),
            monto_cuota = round(tarifa.precio / self.get_cuotas()),
            alquiler_id_alquiler = Alquiler.objects.get(
                id_alquiler = new_alquiler.id_alquiler
            )
        )
        inicio_split = self.get_inicio().split('-')
        fin_split = self.get_fin().split('-')

        inicio_date = date(int(inicio_split[0]), int(inicio_split[1]), int(inicio_split[2]))
        fin_date = date(int(fin_split[0]), int(fin_split[1]), int(fin_split[2]))

        periodo_total = fin_date - inicio_date
        date_cuotas = periodo_total / (self.get_cuotas())

        fechas = []
        for i in range(0, self.get_cuotas()):
            if (i == 0):
                fechas.append(inicio_date + date_cuotas)
            else:
                if (i == self.get_cuotas()):
                    fechas.append(self.get_fin())
                else:
                    fechas.append(fechas[i - 1] + date_cuotas)
        print("los pagos por cuotas son")

        for i in range(0,self.get_cuotas()):
            PagosAlquileres.objects.create(
                nro_cuota=(i+1),
                estado_cuota='DEUDA',
                fecha=fechas[i],
                plan_pagos_id_plan_de_pagos=PlanPagos.objects.get(
                    id_plan_de_pagos= plan_pagos.id_plan_de_pagos
                )
            )
            print(i)
            print(fechas[i])

    def definirFinAlquiler(self,tarifa):
        cursor = connection.cursor()
        cursor.execute('''
        SELECT adddate(%r, interval %r month) as fin
        '''%(self.get_inicio(),tarifa))
        total = dictfetchall(cursor)
        print (total[0])
        return total[0]


    def listar_Alquileres(self):
        cursor = connection.cursor()
        cursor.execute('''
        SELECT c.id_alquiler as id, a.ci as ci,
        a.nombre as nombre, b.placa as placa, c.estado as estado
        from cliente a, vehiculo b, alquiler c
        where a.id_cliente=b.cliente_id
        and a.id_cliente=c.cliente_id_cliente
        and b.id_vehiculo=c.vehiculo_id_vehiculo
        order by(c.estado)
                     ''')
        total = dictfetchall(cursor)
        return total
    def listarAlquilerPorCiCliente(self,ci_cliente):
        cursor = connection.cursor()
        cursor.execute('''
        SELECT c.id_alquiler as id, a.ci as ci,
         a.nombre as nombre, b.placa as placa, c.estado as estado
        from cliente a, vehiculo b, alquiler c
        where a.id_cliente=b.cliente_id
        and a.id_cliente=c.cliente_id_cliente
        and b.id_vehiculo=c.vehiculo_id_vehiculo
        and a.ci=%r
        order by(c.estado)
                     '''%(ci_cliente))
        total = dictfetchall(cursor)
        return total


    def buscarAlquilerPorId(self, alquilerId):
        cursor = connection.cursor()
        cursor.execute('''
        select d.nombre, d.ci, b.meses, c.num_cuotas
        from alquiler a, tarifa_alquiler b, plan_pagos c, cliente d
        where a.id_alquiler=c.alquiler_id_alquiler
        and a.id_tarifa_alquiler=b.id_tarifa_alquiler
        and a.cliente_id_cliente=d.id_cliente
        and a.id_alquiler=%r
        '''%(alquilerId))

        total = dictfetchall(cursor)
        return total[0]

    def listar_cuotas_alquilerPorId(self,alquilerId):
        cursor = connection.cursor()
        cursor.execute('''
        select a.id_pago_cuotas as id, a.fecha as fecha,
        a.estado_cuota as estado, a.nro_cuota as n_cuota,
        b.monto_cuota as monto
        from pagos_alquileres a, plan_pagos b, alquiler c
        where a.plan_pagos_id_plan_de_pagos=b.id_plan_de_pagos
        and b.alquiler_id_alquiler=c.id_alquiler
        and c.id_alquiler=%r
        ''' % (alquilerId))
        total = dictfetchall(cursor)
        return total

    def verificarVehiculoALquiler(self,placa):
        cursor = connection.cursor()
        cursor.execute('''
        select b.id_vehiculo
        from alquiler a, vehiculo b
        where a.estado='ACTIVO'
        and a.vehiculo_id_vehiculo=b.id_vehiculo
        and b.placa=%r
        '''%(placa))
        total = dictfetchall(cursor)
        return total

    def pagarCuotaAlquiler(self, id_cuota):

        pg = PagosAlquileres.objects.get(id_pago_cuotas=id_cuota)
        pg.estado_cuota = "PAGADO"
        pg.save()

        obj_plan_pagos =  PlanPagos.objects.get(
            id_plan_de_pagos = pg.plan_pagos_id_plan_de_pagos.id_plan_de_pagos
        )

        caja = RegistroCaja.objects.get(
            estado='ACTIVO'
        )
        caja.monto_facturado = caja.monto_facturado + pg.plan_pagos_id_plan_de_pagos.monto_cuota
        caja.save()

        id_alquiler = obj_plan_pagos.alquiler_id_alquiler.id_alquiler
        monto = pg.plan_pagos_id_plan_de_pagos.monto_cuota

        return id_alquiler, monto











