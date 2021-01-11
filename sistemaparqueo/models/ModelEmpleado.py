from db.models import dictfetchall, Usuario, TipoUsuario, ControlHorario
from sistemaparqueo.models.ModelUsuario import ModelUsuario
from django.db import connection

class ModelEmpleado(ModelUsuario):

    def __init__(self,):
        self.__hora_ingreso=None
        self.__hora_salida=None
        self.__ci = None
        pass

    def set_hora_ingreso(self,hora_ingreso):
        self.__hora_ingreso=hora_ingreso
    def get_hora_ingreso(self):
        return self.__hora_ingreso

    def set_hora_salida(self,hora_salida):
        self.__hora_salida=hora_salida
    def get_hora_salida(self):
        return self.__hora_salida

    def listaEmpleados(self):
        cursor = connection.cursor()
        cursor.execute('''
                    select viewGestionDeEmpleados.id_usuario as id, viewGestionDeEmpleados.ci as ci, viewGestionDeEmpleados.nombre, viewGestionDeEmpleados.hora_ingreso, viewGestionDeEmpleados.hora_salida
                    from usuario viewGestionDeEmpleados
                    where viewGestionDeEmpleados.id_tipo_usuario=2
                                 ''')
        total = dictfetchall(cursor)
        return total

    def agregarEmpleado(self):

        Usuario.objects.create(
            ci = self.get_ci(),
            nombre = self.get_nombre(),
            usuario = self.get_nombre_usuario(),
            password = self.get_password(),
            hora_ingreso = self.get_hora_ingreso(),
            hora_salida = self.get_hora_salida(),
            id_tipo_usuario = TipoUsuario.objects.get(id_tipo_usuario=2)
        )

    def editarEmpleado(self, EmpleadoId):
        emp = Usuario.objects.get(id_usuario=EmpleadoId)
        emp.ci=self.get_ci()
        emp.nombre=self.get_nombre()
        emp.usuario=self.get_nombre_usuario()
        emp.password=self.get_password()
        emp.hora_ingreso=self.get_hora_ingreso()
        emp.hora_salida=self.get_hora_salida()
        emp.save()

    def listarEntradaDeEmpleados(self):
        cursor = connection.cursor()
        cursor.execute('''
        select a.fecha, a.ingreso, a.salida, b.nombre, b.hora_ingreso, b.hora_salida
        from control_horario a, usuario b
        where a.usuario_id_usuario=b.id_usuario
        and a.salida is not null
         ''')
        total = dictfetchall(cursor)
        return total

    def listarEntradaDeEmpleados_filtroCi(self):
        cursor = connection.cursor()
        cursor.execute('''
                select a.fecha, a.ingreso, a.salida, b.nombre, b.hora_ingreso, b.hora_salida
                from control_horario a, usuario b
                where a.usuario_id_usuario=b.id_usuario
                and a.salida is not null
                and b.ci=%r
                 '''%(self.get_ci()))
        total = dictfetchall(cursor)
        return total

    def listarEntradaDeEmpleados_filtroFecha(self, fecha):
        cursor = connection.cursor()
        cursor.execute('''
                select a.fecha, a.ingreso, a.salida, b.nombre, b.hora_ingreso, b.hora_salida
                from control_horario a, usuario b
                where a.usuario_id_usuario=b.id_usuario
                and a.salida is not null
                and a.fecha=%r
                 '''%(fecha))
        total = dictfetchall(cursor)
        return total

    def listarEntradaDeEmpleados_filtro_Ci_Fecha(self, fecha):
        cursor = connection.cursor()
        cursor.execute('''
                select a.fecha, a.ingreso, a.salida, b.nombre, b.hora_ingreso, b.hora_salida
                from control_horario a, usuario b
                where a.usuario_id_usuario=b.id_usuario
                and b.ci=%r
                and a.fecha=%r
                 '''%(self.get_ci(),fecha))
        total = dictfetchall(cursor)
        return total

    def registrarHorarioEntrada(self,fecha_p, hora_p, id_usuario_p):
        ControlHorario.objects.create(
            fecha=fecha_p,
            ingreso=hora_p,
            usuario_id_usuario=Usuario.objects.get(
                id_usuario=id_usuario_p
            )
        )

    def registrarHorarioSalida(self,hora_salida):
        control_horario=ControlHorario.objects.get(
            salida=None
        )
        control_horario.salida=hora_salida
        control_horario.save()

