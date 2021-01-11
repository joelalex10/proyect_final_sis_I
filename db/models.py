# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alquiler(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    inicio = models.DateField()
    fin = models.DateField()
    estado = models.CharField(max_length=20)
    cliente_id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_id_cliente')
    id_tarifa_alquiler = models.ForeignKey('TarifaAlquiler', models.DO_NOTHING, db_column='id_tarifa_alquiler')
    vehiculo_id_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_id_vehiculo')

    class Meta:
        managed = False
        db_table = 'alquiler'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=30)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cliente'


class ControlHorario(models.Model):
    id_control_horario = models.AutoField(primary_key=True)
    fecha = models.DateField()
    ingreso = models.TimeField()
    salida = models.TimeField(blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'control_horario'


class Descuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    monto = models.FloatField()
    id_registro_parqueo = models.ForeignKey('RegistroParqueo', models.DO_NOTHING, db_column='id_registro_parqueo')

    class Meta:
        managed = False
        db_table = 'descuento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=45)
    nombre = models.CharField(max_length=30)
    autorizacion = models.CharField(max_length=40, blank=True, null=True)
    razon_social = models.CharField(max_length=40)
    direccion = models.TextField()
    contacto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empresa'


class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    posicion = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)
    id_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='id_sector')
    tipo_espacio_id_tipo_espacio = models.ForeignKey('TipoEspacio', models.DO_NOTHING, db_column='tipo_espacio_id_tipo_espacio')

    class Meta:
        managed = False
        db_table = 'espacio'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    codigo_control = models.CharField(max_length=30, blank=True, null=True)
    nro_factura = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField()
    empresa_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id_empresa')
    alquiler_id_alquiler = models.ForeignKey(Alquiler, models.DO_NOTHING, db_column='alquiler_id_alquiler', blank=True, null=True)
    registro_parqueo_id_parqueo = models.ForeignKey('RegistroParqueo', models.DO_NOTHING, db_column='registro_parqueo_id_parqueo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Incidentes(models.Model):
    id_incidentes = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    id_registro_parqueo = models.ForeignKey('RegistroParqueo', models.DO_NOTHING, db_column='id_registro_parqueo')

    class Meta:
        managed = False
        db_table = 'incidentes'


class PagosAlquileres(models.Model):
    id_pago_cuotas = models.AutoField(primary_key=True)
    nro_cuota = models.IntegerField()
    estado_cuota = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    plan_pagos_id_plan_de_pagos = models.ForeignKey('PlanPagos', models.DO_NOTHING, db_column='plan_pagos_id_plan_de_pagos')

    class Meta:
        managed = False
        db_table = 'pagos_alquileres'


class PlanPagos(models.Model):
    id_plan_de_pagos = models.AutoField(primary_key=True)
    monto_cuota = models.FloatField()
    num_cuotas = models.IntegerField()
    alquiler_id_alquiler = models.ForeignKey(Alquiler, models.DO_NOTHING, db_column='alquiler_id_alquiler')

    class Meta:
        managed = False
        db_table = 'plan_pagos'


class RegistroCaja(models.Model):
    id_registro_caja = models.AutoField(primary_key=True)
    hora_apertura = models.TimeField()
    hora_clausura = models.TimeField(blank=True, null=True)
    monto_apertura = models.FloatField()
    monto_clausura = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=40)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()
    monto_facturado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_caja'


class RegistroParqueo(models.Model):
    id_parqueo = models.AutoField(primary_key=True)
    entrada = models.DateTimeField()
    salida = models.DateTimeField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING)
    id_espacio = models.ForeignKey(Espacio, models.DO_NOTHING, db_column='id_espacio')
    id_tarifas = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='id_tarifas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_parqueo'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'sector'


class Tarifa(models.Model):
    id_tarifas = models.AutoField(primary_key=True)
    horas = models.IntegerField()
    dias = models.IntegerField()
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tarifa'


class TarifaAlquiler(models.Model):
    id_tarifa_alquiler = models.AutoField(primary_key=True)
    meses = models.IntegerField()
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tarifa_alquiler'


class TipoEspacio(models.Model):
    id_tipo_espacio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_espacio'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    ci = models.CharField(max_length=30)
    nombre = models.CharField(max_length=45)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    hora_ingreso = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=30)
    marca_modelo = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=15)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehiculo'

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]