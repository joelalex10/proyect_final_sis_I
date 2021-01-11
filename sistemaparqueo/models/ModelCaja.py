from django.db import connection

from db.models import dictfetchall, RegistroCaja, Usuario


class ModelCaja():
    def __init__(self):
        self.__fecha=None
        self.__hora_entrada=None
        self.__hora_cierre=None
        self.__monto_apertura=None
        self.__monto_cierre=None
        self.__estado=None

    def set_monto_apertura(self,monto_apertura):
        self.__monto_apertura=monto_apertura
    def get_monto_apertura(self):
        return self.__monto_apertura

    def set_monto_cierre(self,monto_cierre):
        self.__monto_cierre=monto_cierre
    def get_monto_cierre(self):
        return self.__monto_cierre

    def set_estado(self,estado):
        self.__estado=estado
    def get_estado(self):
        return self.__estado

    def set_hora_entrada(self,hora_entrada):
        self.__hora_entrada=hora_entrada
    def get_hora_entrada(self):
        return self.__hora_entrada

    def set_hora_cierre(self,hora_cierre):
        self.__hora_cierre=hora_cierre
    def get_hora_cierre(self):
        return self.__hora_cierre

    def set_fecha(self,fecha):
        self.__fecha=fecha
    def get_fecha(self):
        return self.__fecha


    def registrarAperturaCaja(self,usuario):
        RegistroCaja.objects.create(
            hora_apertura = self.get_hora_entrada(),
            monto_apertura = self.get_monto_apertura(),
            estado = self.get_estado(),
            id_usuario = Usuario.objects.get(
                id_usuario=usuario
            ),
            monto_facturado=0,
            fecha=self.get_fecha()
        )
    def registrarCierreCaja(self,cajaId):
        caja = RegistroCaja.objects.get(
            id_registro_caja = cajaId
        )
        caja.estado=self.get_estado()
        caja.hora_clausura=self.get_hora_cierre()
        caja.monto_clausura=self.get_monto_cierre()
        caja.save()


    def verificarEstadoCaja(self):
        cursor = connection.cursor()
        cursor.execute('''
        select *
        from registro_caja
        where estado=%r
        '''%(self.get_estado()))
        total = dictfetchall(cursor)
        return total

    def convertirLiteralMonto(self,numero):
        indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
        entero = int(numero)
        decimal = int(round((numero - entero) * 100))
        # print 'decimal : ',decimal
        contador = 0
        numero_letras = ""
        while entero > 0:
            a = entero % 1000
            if contador == 0:
                en_letras = self.__convierte_cifra(a, 1).strip()
            else:
                en_letras = self.__convierte_cifra(a, 0).strip()
            if a == 0:
                numero_letras = en_letras + " " + numero_letras
            elif a == 1:
                if contador in (1, 3):
                    numero_letras = indicador[contador][0] + " " + numero_letras
                else:
                    numero_letras = en_letras + " " + indicador[contador][0] + " " + numero_letras
            else:
                numero_letras = en_letras + " " + indicador[contador][1] + " " + numero_letras
            numero_letras = numero_letras.strip()
            contador = contador + 1
            entero = int(entero / 1000)
            if not numero_letras:
                numero_letras = "CERO"

        numero_letras = numero_letras + " CON " + str(decimal) + "/100 BOLIVIANOS"
        # return
        # 'numero: ', numero
        return numero_letras

    def __convierte_cifra(self,numero, sw):
        lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS",
                         "SEISCIENTOS",
                         "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
        lista_decena = ["", (
            "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"),
                        ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y "), ("CUARENTA", "CUARENTA Y "),
                        ("CINCUENTA", "CINCUENTA Y "), ("SESENTA", "SESENTA Y "),
                        ("SETENTA", "SETENTA Y "), ("OCHENTA", "OCHENTA Y "),
                        ("NOVENTA", "NOVENTA Y ")
                        ]
        lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
        centena = int(numero / 100)
        decena = int((numero - (centena * 100)) / 10)
        unidad = int(numero - (centena * 100 + decena * 10))
        # print "centena: ",centena, "decena: ",decena,'unidad: ',unidad

        texto_centena = ""
        texto_decena = ""
        texto_unidad = ""

        # Validad las centenas
        texto_centena = lista_centana[centena]
        if centena == 1:
            if (decena + unidad) != 0:
                texto_centena = texto_centena[1]
            else:
                texto_centena = texto_centena[0]

        # Valida las decenas
        texto_decena = lista_decena[decena]
        if decena == 1:
            texto_decena = texto_decena[unidad]
        elif decena > 1:
            if unidad != 0:
                texto_decena = texto_decena[1]
            else:
                texto_decena = texto_decena[0]
        # Validar las unidades
        # print "texto_unidad: ",texto_unidad
        if decena != 1:
            texto_unidad = lista_unidad[unidad]
            if unidad == 1:
                texto_unidad = texto_unidad[sw]

        return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)
