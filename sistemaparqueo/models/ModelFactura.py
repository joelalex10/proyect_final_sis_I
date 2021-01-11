from db.models import Factura, Empresa, RegistroParqueo, Alquiler, dictfetchall
from datetime import datetime
from django.db import connection
import math
import re

class ModelFactura():
    def __init__(self):
        self.__codigo_control = None
        self.__numero_factura = None

    def set_codigo_control(self,codigo_control):
        self.__codigo_control=codigo_control
    def get_codigo_control(self):
        return self.__codigo_control

    def set_numero_factura(self,numero_factura):
        self.__numero_factura=numero_factura
    def get_numero_factura(self):
        return self.__numero_factura

    def agregarReciboSalidaVehiculo(self, idRegistro):
        Factura.objects.create(
            empresa_id_empresa=Empresa.objects.get(
                id_empresa = 1
            ),
            registro_parqueo_id_parqueo=RegistroParqueo.objects.get(
                id_parqueo = idRegistro
            ),
            fecha=format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
    def agregarFacturaAlquiler(self, alquiler_Id):
        new_factura = Factura.objects.create(
            codigo_control = self.get_codigo_control(),
            nro_factura = self.get_numero_factura(),
            empresa_id_empresa=Empresa.objects.get(
                id_empresa=1
            ),
            alquiler_id_alquiler = Alquiler.objects.get(
                id_alquiler= alquiler_Id
            ),
            fecha = format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        return new_factura

    def obtenerDatosParaFactura(self, facturaId):
        cursor = connection.cursor()
        cursor.execute('''
        select d.nit, d.direccion, b.nro_factura, d.autorizacion, b.fecha,
        e.nombre, e.ci, c.monto_cuota, b.codigo_control
        from alquiler a, factura b, plan_pagos c, empresa d, cliente e
        where a.id_alquiler=b.alquiler_id_alquiler
        and a.id_alquiler=c.alquiler_id_alquiler
        and b.empresa_id_empresa=d.id_empresa
        and a.cliente_id_cliente = e.id_cliente
        and b.id_factura=%r
        '''%(facturaId))
        total = dictfetchall(cursor)
        return total

    def generarCodigoControl(self, auth, nit, number, date, total, key):
        code = ''
        number = self.__verhoeff(number, 2)
        nit = self.__verhoeff(nit, 2)
        date = self.__verhoeff(date, 2)
        total = self.__verhoeff(total, 2)
        vf = self.__verhoeff(str(
            int(number) +
            int(nit) +
            int(date) +
            int(total)
        ), 5)[-5:]

        input = [auth, number, nit, date, total]
        idx = 0
        for i in range(5):
            code += input[i] + key[idx:idx + 1 + int(vf[i])]
            idx += 1 + int(vf[i])
        code = self.__arc4(code, key + vf)

        final_sum = 0
        total_sum = 0
        partial_sum = [0, 0, 0, 0, 0]
        for i in range(len(code)):
            partial_sum[i % 5] += ord(code[i])
            total_sum += ord(code[i])
        for i in range(5):
            final_sum += math.floor((total_sum * partial_sum[i]) / (1 + int(vf[i])))

        matched = []
        for regexp in re.findall('.{2}', self.__arc4(self.__base64(final_sum), key + vf)):
            matched.append(regexp)
        code = '-'.join(matched)

        return code

    def __verhoeff(self, num, times):
        d = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
            [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
            [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
            [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
            [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
            [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ]
        p = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
            [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
            [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
            [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
            [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
        ]
        inv = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
        for i in range(times, 0, -1):
            c = 0
            for i in range(len(num) - 1, -1, -1):
                c = d[c][p[((len(num) - i) % 8)][int(num[i])]]
            num += str(inv[c])
        return num

    def __arc4(self, msg, key):
        state = [i for i in range(256)]
        j = 0
        for i in range(256):
            j = (j + state[i] + ord(key[i % len(key)])) % 256
            temp = state[i]
            state[i] = state[j]
            state[j] = temp
        x = y = 0
        output = ''
        for i in range(len(msg)):
            x = (x + 1) % 256
            y = (state[x] + y) % 256
            temp = state[x]
            state[x] = state[y]
            state[y] = temp
            output += "{:02x}".format(ord(msg[i]) ^ state[(state[x] + state[y]) % 256])
        return output.upper()

    def __base64(self,number):
        result = ''
        dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
        while number > 0:
            result = dic[int(number % 64)] + result
            number = math.floor(number / 64)
        return result

