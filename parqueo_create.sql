-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-12-31 16:21:06.1

-- tables
-- Table: alquiler
CREATE TABLE alquiler (
    id_alquiler int NOT NULL AUTO_INCREMENT,
    inicio date NOT NULL,
    fin date NOT NULL,
    estado varchar(20) NOT NULL,
    cliente_id_cliente int NOT NULL,
    id_tarifa_alquiler int NOT NULL,
    CONSTRAINT alquiler_pk PRIMARY KEY (id_alquiler)
);

-- Table: cliente
CREATE TABLE cliente (
    id_cliente int NOT NULL AUTO_INCREMENT,
    ci varchar(30) NOT NULL,
    nombre varchar(45) NOT NULL,
    CONSTRAINT cliente_pk PRIMARY KEY (id_cliente)
);

-- Table: control_horario
CREATE TABLE control_horario (
    id_control_horario int NOT NULL AUTO_INCREMENT,
    fecha date NOT NULL,
    ingreso time NOT NULL,
    salida time NOT NULL,
    usuario_id_usuario int NOT NULL,
    CONSTRAINT control_horario_pk PRIMARY KEY (id_control_horario)
);

-- Table: descuento
CREATE TABLE descuento (
    id_descuento int NOT NULL AUTO_INCREMENT,
    descripcion text NOT NULL,
    monto double NOT NULL,
    id_registro_parqueo int NOT NULL,
    CONSTRAINT descuento_pk PRIMARY KEY (id_descuento)
);

-- Table: empresa
CREATE TABLE empresa (
    id_empresa int NOT NULL AUTO_INCREMENT,
    nit varchar(45) NOT NULL,
    nombre varchar(30) NOT NULL,
    razon_social varchar(40) NOT NULL,
    direccion text NOT NULL,
    contacto varchar(45) NOT NULL,
    CONSTRAINT empresa_pk PRIMARY KEY (id_empresa)
);

-- Table: espacio
CREATE TABLE espacio (
    id_espacio int NOT NULL AUTO_INCREMENT,
    posicion varchar(20) NOT NULL,
    estado varchar(30) NOT NULL,
    id_sector int NOT NULL,
    tipo_espacio_id_tipo_espacio int NOT NULL,
    CONSTRAINT espacio_pk PRIMARY KEY (id_espacio)
);

-- Table: factura
CREATE TABLE factura (
    id_factura int NOT NULL AUTO_INCREMENT,
    codigo_control varchar(30) NOT NULL,
    autorizacion int NOT NULL,
    empresa_id_empresa int NOT NULL,
    alquiler_id_alquiler int NOT NULL,
    registro_parqueo_id_parqueo int NOT NULL,
    CONSTRAINT factura_pk PRIMARY KEY (id_factura)
);

-- Table: incidentes
CREATE TABLE incidentes (
    id_incidentes int NOT NULL AUTO_INCREMENT,
    descripcion text NOT NULL,
    id_registro_parqueo int NOT NULL,
    CONSTRAINT incidentes_pk PRIMARY KEY (id_incidentes)
);

-- Table: pagos_alquileres
CREATE TABLE pagos_alquileres (
    id_pago_cuotas int NOT NULL,
    nro_cuota int NOT NULL,
    estado_cuota int NOT NULL,
    fecha datetime NOT NULL,
    plan_pagos_id_plan_de_pagos int NOT NULL,
    CONSTRAINT pagos_alquileres_pk PRIMARY KEY (id_pago_cuotas)
);

-- Table: plan_pagos
CREATE TABLE plan_pagos (
    id_plan_de_pagos int NOT NULL AUTO_INCREMENT,
    monto_cuota double NOT NULL,
    num_cuotas int NOT NULL,
    alquiler_id_alquiler int NOT NULL,
    CONSTRAINT plan_pagos_pk PRIMARY KEY (id_plan_de_pagos)
);

-- Table: registro_caja
CREATE TABLE registro_caja (
    id_registro_caja int NOT NULL AUTO_INCREMENT,
    fecha datetime NOT NULL,
    monto double NOT NULL,
    tipo varchar(40) NOT NULL,
    id_usuario int NOT NULL,
    CONSTRAINT registro_caja_pk PRIMARY KEY (id_registro_caja)
);

-- Table: registro_parqueo
CREATE TABLE registro_parqueo (
    id_parqueo int NOT NULL AUTO_INCREMENT,
    entrada datetime NOT NULL,
    salida datetime NOT NULL,
    id_usuario int NOT NULL,
    vehiculo_id int NOT NULL,
    id_espacio int NOT NULL,
    id_tarifas int NULL,
    CONSTRAINT registro_parqueo_pk PRIMARY KEY (id_parqueo)
);

-- Table: sector
CREATE TABLE sector (
    id_sector int NOT NULL,
    sector varchar(10) NOT NULL,
    CONSTRAINT sector_pk PRIMARY KEY (id_sector)
);

-- Table: tarifa
CREATE TABLE tarifa (
    id_tarifas int NOT NULL AUTO_INCREMENT,
    horas int NOT NULL,
    dias int NOT NULL,
    precio decimal(4,2) NOT NULL,
    CONSTRAINT tarifa_pk PRIMARY KEY (id_tarifas)
);

-- Table: tarifa_alquiler
CREATE TABLE tarifa_alquiler (
    id_tarifa_alquiler int NOT NULL AUTO_INCREMENT,
    meses int NOT NULL,
    precio double NOT NULL,
    CONSTRAINT tarifa_alquiler_pk PRIMARY KEY (id_tarifa_alquiler)
);

-- Table: tipo_espacio
CREATE TABLE tipo_espacio (
    id_tipo_espacio int NOT NULL AUTO_INCREMENT,
    tipo varchar(20) NOT NULL,
    CONSTRAINT tipo_espacio_pk PRIMARY KEY (id_tipo_espacio)
);

-- Table: tipo_usuario
CREATE TABLE tipo_usuario (
    id_tipo_usuario int NOT NULL AUTO_INCREMENT,
    tipo varchar(45) NOT NULL,
    CONSTRAINT tipo_usuario_pk PRIMARY KEY (id_tipo_usuario)
);

-- Table: tipo_vehiculo
CREATE TABLE tipo_vehiculo (
    id_tipo_vehiculo int NOT NULL AUTO_INCREMENT,
    tipo varchar(45) NOT NULL,
    CONSTRAINT tipo_vehiculo_pk PRIMARY KEY (id_tipo_vehiculo)
);

-- Table: usuario
CREATE TABLE usuario (
    id_usuario int NOT NULL AUTO_INCREMENT,
    ci varchar(30) NOT NULL,
    nombre varchar(45) NOT NULL,
    usuario varchar(30) NOT NULL,
    password varchar(30) NOT NULL,
    hora_ingreso time NULL,
    hora_salida time NULL,
    id_tipo_usuario int NOT NULL,
    CONSTRAINT usuario_pk PRIMARY KEY (id_usuario)
);

-- Table: vehiculo
CREATE TABLE vehiculo (
    id_vehiculo int NOT NULL AUTO_INCREMENT,
    placa varchar(30) NOT NULL,
    marca_modelo varchar(45) NULL,
    color varchar(15) NOT NULL,
    cliente_id int NULL,
    tipo_vehiculo_id int NOT NULL,
    CONSTRAINT vehiculo_pk PRIMARY KEY (id_vehiculo)
);

-- foreign keys
-- Reference: alquiler_cliente (table: alquiler)
ALTER TABLE alquiler ADD CONSTRAINT alquiler_cliente FOREIGN KEY alquiler_cliente (cliente_id_cliente)
    REFERENCES cliente (id_cliente);

-- Reference: alquiler_tarifa_alquiler (table: alquiler)
ALTER TABLE alquiler ADD CONSTRAINT alquiler_tarifa_alquiler FOREIGN KEY alquiler_tarifa_alquiler (id_tarifa_alquiler)
    REFERENCES tarifa_alquiler (id_tarifa_alquiler);

-- Reference: control_horario_usuario (table: control_horario)
ALTER TABLE control_horario ADD CONSTRAINT control_horario_usuario FOREIGN KEY control_horario_usuario (usuario_id_usuario)
    REFERENCES usuario (id_usuario);

-- Reference: descuento_registro_parqueo (table: descuento)
ALTER TABLE descuento ADD CONSTRAINT descuento_registro_parqueo FOREIGN KEY descuento_registro_parqueo (id_registro_parqueo)
    REFERENCES registro_parqueo (id_parqueo);

-- Reference: espacio_sector (table: espacio)
ALTER TABLE espacio ADD CONSTRAINT espacio_sector FOREIGN KEY espacio_sector (id_sector)
    REFERENCES sector (id_sector);

-- Reference: espacio_tipo_espacio (table: espacio)
ALTER TABLE espacio ADD CONSTRAINT espacio_tipo_espacio FOREIGN KEY espacio_tipo_espacio (tipo_espacio_id_tipo_espacio)
    REFERENCES tipo_espacio (id_tipo_espacio);

-- Reference: factura_alquiler (table: factura)
ALTER TABLE factura ADD CONSTRAINT factura_alquiler FOREIGN KEY factura_alquiler (alquiler_id_alquiler)
    REFERENCES alquiler (id_alquiler);

-- Reference: factura_empresa (table: factura)
ALTER TABLE factura ADD CONSTRAINT factura_empresa FOREIGN KEY factura_empresa (empresa_id_empresa)
    REFERENCES empresa (id_empresa);

-- Reference: factura_registro_parqueo (table: factura)
ALTER TABLE factura ADD CONSTRAINT factura_registro_parqueo FOREIGN KEY factura_registro_parqueo (registro_parqueo_id_parqueo)
    REFERENCES registro_parqueo (id_parqueo);

-- Reference: incidentes_registro_parqueo (table: incidentes)
ALTER TABLE incidentes ADD CONSTRAINT incidentes_registro_parqueo FOREIGN KEY incidentes_registro_parqueo (id_registro_parqueo)
    REFERENCES registro_parqueo (id_parqueo);

-- Reference: pagos_alquileres_plan_pagos (table: pagos_alquileres)
ALTER TABLE pagos_alquileres ADD CONSTRAINT pagos_alquileres_plan_pagos FOREIGN KEY pagos_alquileres_plan_pagos (plan_pagos_id_plan_de_pagos)
    REFERENCES plan_pagos (id_plan_de_pagos);

-- Reference: plan_pagos_alquiler (table: plan_pagos)
ALTER TABLE plan_pagos ADD CONSTRAINT plan_pagos_alquiler FOREIGN KEY plan_pagos_alquiler (alquiler_id_alquiler)
    REFERENCES alquiler (id_alquiler);

-- Reference: registro_caja_usuario (table: registro_caja)
ALTER TABLE registro_caja ADD CONSTRAINT registro_caja_usuario FOREIGN KEY registro_caja_usuario (id_usuario)
    REFERENCES usuario (id_usuario);

-- Reference: registro_parqueo_espacio (table: registro_parqueo)
ALTER TABLE registro_parqueo ADD CONSTRAINT registro_parqueo_espacio FOREIGN KEY registro_parqueo_espacio (id_espacio)
    REFERENCES espacio (id_espacio);

-- Reference: registro_parqueo_tarifa (table: registro_parqueo)
ALTER TABLE registro_parqueo ADD CONSTRAINT registro_parqueo_tarifa FOREIGN KEY registro_parqueo_tarifa (id_tarifas)
    REFERENCES tarifa (id_tarifas);

-- Reference: registro_parqueo_usuario (table: registro_parqueo)
ALTER TABLE registro_parqueo ADD CONSTRAINT registro_parqueo_usuario FOREIGN KEY registro_parqueo_usuario (id_usuario)
    REFERENCES usuario (id_usuario);

-- Reference: registro_parqueo_vehiculo (table: registro_parqueo)
ALTER TABLE registro_parqueo ADD CONSTRAINT registro_parqueo_vehiculo FOREIGN KEY registro_parqueo_vehiculo (vehiculo_id)
    REFERENCES vehiculo (id_vehiculo);

-- Reference: usuario_tipo_usuario (table: usuario)
ALTER TABLE usuario ADD CONSTRAINT usuario_tipo_usuario FOREIGN KEY usuario_tipo_usuario (id_tipo_usuario)
    REFERENCES tipo_usuario (id_tipo_usuario);

-- Reference: vehiculo_cliente (table: vehiculo)
ALTER TABLE vehiculo ADD CONSTRAINT vehiculo_cliente FOREIGN KEY vehiculo_cliente (cliente_id)
    REFERENCES cliente (id_cliente);

-- Reference: vehiculo_tipo_vehiculo (table: vehiculo)
ALTER TABLE vehiculo ADD CONSTRAINT vehiculo_tipo_vehiculo FOREIGN KEY vehiculo_tipo_vehiculo (tipo_vehiculo_id)
    REFERENCES tipo_vehiculo (id_tipo_vehiculo);

-- End of file.

