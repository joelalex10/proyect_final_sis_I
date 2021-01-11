from db.models import dictfetchall
from sistemaparqueo.models.ModelUsuario import ModelUsuario
from django.db import connection

class ModelAdministrador(ModelUsuario):

    def __init__(self,):
        pass

    def mostrarReporteCaja(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.fecha, b.nombre, a.monto_apertura, a.monto_facturado,
        a.monto_clausura, ((a.monto_apertura  + a.monto_facturado ) - a.monto_clausura) as diferencias
        from registro_caja a, usuario b
        where a.id_usuario=b.id_usuario
        and a.estado='CERRADO'
        order by a.fecha desc
            ''')
        results = dictfetchall(cursor)
        return results

    def mostrarReporteCajaConFiltros(self,fecha):
        mes_split = fecha.split('-')
        anio = mes_split[0]
        mes = mes_split[1]
        cursor = connection.cursor()
        cursor.execute('''
                        select a.fecha, b.nombre, a.monto_apertura, a.monto_facturado, a.monto_clausura,
                         ((a.monto_facturado + a.monto_apertura ) - a.monto_clausura) as diferencias
                         from registro_caja a, usuario b
                         where a.id_usuario=b.id_usuario
                         and month(a.fecha)=%r
                         and year(a.fecha)=%r
                         and a.estado='CERRADO'
                         order by a.fecha
                         ''' % (mes, anio))
        results = dictfetchall(cursor)
        return results

    def mostrarTotalReporteCaja(self):
        cursor = connection.cursor()
        cursor.execute('''
                select sum(a.monto_apertura) as monto_apertura, sum(a.monto_facturado) as monto_facturado,
                sum(a.monto_clausura) as monto_clausura, sum(((a.monto_facturado + a.monto_apertura ) - a.monto_clausura)) as diferencias
                from registro_caja a, usuario b
                where a.id_usuario=b.id_usuario
                and a.estado='CERRADO'
                ''')
        results = dictfetchall(cursor)
        return results

    def mostrarTotalReporteCajaConFiltros(self,fecha):
        mes_split = fecha.split('-')
        anio = mes_split[0]
        mes = mes_split[1]
        cursor1 = connection.cursor()
        cursor1.execute('''
                    select sum(a.monto_apertura) as monto_apertura, sum(a.monto_facturado) as monto_facturado,
                    sum(a.monto_clausura) as monto_clausura,
                    sum(((a.monto_facturado + a.monto_apertura ) - a.monto_clausura)) as diferencias
                    from registro_caja a, usuario b
                    where a.id_usuario=b.id_usuario
                    and a.estado='CERRADO'
                    and month(a.fecha)=%r
                    and year(a.fecha)=%r    
                         ''' % (mes, anio))
        total = dictfetchall(cursor1)
        return total





