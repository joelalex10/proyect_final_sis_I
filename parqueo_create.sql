create table auth_group
(
    id   int auto_increment
        primary key,
    name varchar(150) not null,
    constraint name
        unique (name)
);

create table auth_user
(
    id           int auto_increment
        primary key,
    password     varchar(128) not null,
    last_login   datetime(6)  null,
    is_superuser tinyint(1)   not null,
    username     varchar(150) not null,
    first_name   varchar(150) not null,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     tinyint(1)   not null,
    is_active    tinyint(1)   not null,
    date_joined  datetime(6)  not null,
    constraint username
        unique (username)
);

create table auth_user_groups
(
    id       int auto_increment
        primary key,
    user_id  int not null,
    group_id int not null,
    constraint auth_user_groups_user_id_group_id_94350c0c_uniq
        unique (user_id, group_id),
    constraint auth_user_groups_group_id_97559544_fk_auth_group_id
        foreign key (group_id) references auth_group (id),
    constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

create table cliente
(
    id_cliente int auto_increment
        primary key,
    ci         varchar(30) not null,
    nombre     varchar(45) not null
);

create table django_content_type
(
    id        int auto_increment
        primary key,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    constraint django_content_type_app_label_model_76bd3d3b_uniq
        unique (app_label, model)
);

create table auth_permission
(
    id              int auto_increment
        primary key,
    name            varchar(255) not null,
    content_type_id int          not null,
    codename        varchar(100) not null,
    constraint auth_permission_content_type_id_codename_01ab375a_uniq
        unique (content_type_id, codename),
    constraint auth_permission_content_type_id_2f476e4b_fk_django_co
        foreign key (content_type_id) references django_content_type (id)
);

create table auth_group_permissions
(
    id            int auto_increment
        primary key,
    group_id      int not null,
    permission_id int not null,
    constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
        unique (group_id, permission_id),
    constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
        foreign key (permission_id) references auth_permission (id),
    constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
        foreign key (group_id) references auth_group (id)
);

create table auth_user_user_permissions
(
    id            int auto_increment
        primary key,
    user_id       int not null,
    permission_id int not null,
    constraint auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
        unique (user_id, permission_id),
    constraint auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
        foreign key (permission_id) references auth_permission (id),
    constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
        foreign key (user_id) references auth_user (id)
);

create table django_admin_log
(
    id              int auto_increment
        primary key,
    action_time     datetime(6)       not null,
    object_id       longtext          null,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  longtext          not null,
    content_type_id int               null,
    user_id         int               not null,
    constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
        foreign key (content_type_id) references django_content_type (id),
    constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
        foreign key (user_id) references auth_user (id),
    constraint action_flag
        check (`action_flag` >= 0)
);

create table django_migrations
(
    id      int auto_increment
        primary key,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime(6)  not null
);

create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data longtext    not null,
    expire_date  datetime(6) not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table empresa
(
    id_empresa   int auto_increment
        primary key,
    nit          varchar(45) not null,
    nombre       varchar(30) not null,
    autorizacion varchar(40) null,
    razon_social varchar(40) not null,
    direccion    text        not null,
    contacto     varchar(45) not null
);

create table sector
(
    id_sector int auto_increment
        primary key,
    sector    varchar(10) not null
);

create table tarifa
(
    id_tarifas int auto_increment
        primary key,
    horas      int          not null,
    dias       int          not null,
    precio     double(6, 2) not null
);

create table tarifa_alquiler
(
    id_tarifa_alquiler int auto_increment
        primary key,
    meses              int          not null,
    precio             double(6, 2) not null
);

create table tipo_espacio
(
    id_tipo_espacio int auto_increment
        primary key,
    tipo            varchar(20) not null
);

create table espacio
(
    id_espacio                   int auto_increment
        primary key,
    posicion                     varchar(20) not null,
    estado                       varchar(30) not null,
    id_sector                    int         not null,
    tipo_espacio_id_tipo_espacio int         not null,
    constraint espacio_sector
        foreign key (id_sector) references sector (id_sector),
    constraint espacio_tipo_espacio
        foreign key (tipo_espacio_id_tipo_espacio) references tipo_espacio (id_tipo_espacio)
);

create table tipo_usuario
(
    id_tipo_usuario int auto_increment
        primary key,
    tipo            varchar(45) not null
);

create table tipo_vehiculo
(
    id_tipo_vehiculo int auto_increment
        primary key,
    tipo             varchar(45) not null
);

create table usuario
(
    id_usuario      int auto_increment
        primary key,
    ci              varchar(30) not null,
    nombre          varchar(45) not null,
    usuario         varchar(30) not null,
    password        varchar(30) not null,
    hora_ingreso    time        null,
    hora_salida     time        null,
    id_tipo_usuario int         not null,
    constraint usuario_tipo_usuario
        foreign key (id_tipo_usuario) references tipo_usuario (id_tipo_usuario)
);

create table control_horario
(
    id_control_horario int auto_increment
        primary key,
    fecha              date not null,
    ingreso            time not null,
    salida             time null,
    usuario_id_usuario int  not null,
    constraint control_horario_usuario
        foreign key (usuario_id_usuario) references usuario (id_usuario)
);

create table registro_caja
(
    id_registro_caja int auto_increment
        primary key,
    hora_apertura    time        not null,
    hora_clausura    time        null,
    monto_apertura   double      not null,
    monto_clausura   double      null,
    estado           varchar(40) not null,
    id_usuario       int         not null,
    fecha            date        not null,
    monto_facturado  double      null,
    constraint registro_caja_usuario
        foreign key (id_usuario) references usuario (id_usuario)
);

create table vehiculo
(
    id_vehiculo      int auto_increment
        primary key,
    placa            varchar(30) not null,
    marca_modelo     varchar(45) null,
    color            varchar(15) not null,
    cliente_id       int         null,
    tipo_vehiculo_id int         not null,
    constraint vehiculo_cliente
        foreign key (cliente_id) references cliente (id_cliente),
    constraint vehiculo_tipo_vehiculo
        foreign key (tipo_vehiculo_id) references tipo_vehiculo (id_tipo_vehiculo)
);

create table alquiler
(
    id_alquiler          int auto_increment
        primary key,
    inicio               date        not null,
    fin                  date        not null,
    estado               varchar(20) not null,
    cliente_id_cliente   int         not null,
    id_tarifa_alquiler   int         not null,
    vehiculo_id_vehiculo int         not null,
    constraint alquiler_cliente
        foreign key (cliente_id_cliente) references cliente (id_cliente),
    constraint alquiler_tarifa_alquiler
        foreign key (id_tarifa_alquiler) references tarifa_alquiler (id_tarifa_alquiler),
    constraint alquiler_vehiculo
        foreign key (vehiculo_id_vehiculo) references vehiculo (id_vehiculo)
);

create table plan_pagos
(
    id_plan_de_pagos     int auto_increment
        primary key,
    monto_cuota          double not null,
    num_cuotas           int    not null,
    alquiler_id_alquiler int    not null,
    constraint plan_pagos_alquiler
        foreign key (alquiler_id_alquiler) references alquiler (id_alquiler)
);

create table pagos_alquileres
(
    id_pago_cuotas              int auto_increment
        primary key,
    nro_cuota                   int         not null,
    estado_cuota                varchar(20) not null,
    fecha                       datetime    not null,
    plan_pagos_id_plan_de_pagos int         not null,
    constraint pagos_alquileres_plan_pagos
        foreign key (plan_pagos_id_plan_de_pagos) references plan_pagos (id_plan_de_pagos)
);

create table registro_parqueo
(
    id_parqueo  int auto_increment
        primary key,
    entrada     datetime not null,
    salida      datetime null,
    id_usuario  int      not null,
    vehiculo_id int      not null,
    id_espacio  int      not null,
    id_tarifas  int      null,
    constraint registro_parqueo_espacio
        foreign key (id_espacio) references espacio (id_espacio),
    constraint registro_parqueo_tarifa
        foreign key (id_tarifas) references tarifa (id_tarifas),
    constraint registro_parqueo_usuario
        foreign key (id_usuario) references usuario (id_usuario),
    constraint registro_parqueo_vehiculo
        foreign key (vehiculo_id) references vehiculo (id_vehiculo)
);

create table descuento
(
    id_descuento        int auto_increment
        primary key,
    descripcion         text   not null,
    monto               double not null,
    id_registro_parqueo int    not null,
    constraint descuento_registro_parqueo
        foreign key (id_registro_parqueo) references registro_parqueo (id_parqueo)
);

create table factura
(
    id_factura                  int auto_increment
        primary key,
    codigo_control              varchar(30) null,
    nro_factura                 varchar(45) null,
    fecha                       datetime    not null,
    empresa_id_empresa          int         not null,
    alquiler_id_alquiler        int         null,
    registro_parqueo_id_parqueo int         null,
    constraint factura_alquiler
        foreign key (alquiler_id_alquiler) references alquiler (id_alquiler),
    constraint factura_empresa
        foreign key (empresa_id_empresa) references empresa (id_empresa),
    constraint factura_registro_parqueo
        foreign key (registro_parqueo_id_parqueo) references registro_parqueo (id_parqueo)
);

create table incidentes
(
    id_incidentes       int auto_increment
        primary key,
    descripcion         text not null,
    id_registro_parqueo int  not null,
    constraint incidentes_registro_parqueo
        foreign key (id_registro_parqueo) references registro_parqueo (id_parqueo)
);

