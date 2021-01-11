-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-01-2021 a las 22:57:07
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `parqueo`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `ultimopago` (`id_plan_pago` INT)  select max(fecha)
    from pagos_alquileres a
    where a.plan_pagos_id_plan_de_pagos=id_plan_pago
    and a.estado_cuota='PAGADO'$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alquiler`
--

CREATE TABLE `alquiler` (
  `id_alquiler` int(11) NOT NULL,
  `inicio` date NOT NULL,
  `fin` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `cliente_id_cliente` int(11) NOT NULL,
  `id_tarifa_alquiler` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alquiler`
--

INSERT INTO `alquiler` (`id_alquiler`, `inicio`, `fin`, `estado`, `cliente_id_cliente`, `id_tarifa_alquiler`) VALUES
(1, '2019-01-09', '2019-03-09', 'FINALIZADO', 2, 2),
(2, '2019-01-09', '2019-05-09', 'FINALIZADO', 1, 1),
(3, '2019-01-09', '2019-07-09', 'FINALIZADO', 3, 5),
(4, '2020-11-13', '2021-02-13', 'ACTIVO', 10, 3),
(5, '2020-11-13', '2021-01-13', 'ACTIVO', 8, 2),
(6, '2020-11-13', '2021-03-13', 'ACTIVO', 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add alquiler', 1, 'add_alquiler'),
(2, 'Can change alquiler', 1, 'change_alquiler'),
(3, 'Can delete alquiler', 1, 'delete_alquiler'),
(4, 'Can view alquiler', 1, 'view_alquiler'),
(5, 'Can add cliente', 2, 'add_cliente'),
(6, 'Can change cliente', 2, 'change_cliente'),
(7, 'Can delete cliente', 2, 'delete_cliente'),
(8, 'Can view cliente', 2, 'view_cliente'),
(9, 'Can add control horario', 3, 'add_controlhorario'),
(10, 'Can change control horario', 3, 'change_controlhorario'),
(11, 'Can delete control horario', 3, 'delete_controlhorario'),
(12, 'Can view control horario', 3, 'view_controlhorario'),
(13, 'Can add descuento', 4, 'add_descuento'),
(14, 'Can change descuento', 4, 'change_descuento'),
(15, 'Can delete descuento', 4, 'delete_descuento'),
(16, 'Can view descuento', 4, 'view_descuento'),
(17, 'Can add empresa', 5, 'add_empresa'),
(18, 'Can change empresa', 5, 'change_empresa'),
(19, 'Can delete empresa', 5, 'delete_empresa'),
(20, 'Can view empresa', 5, 'view_empresa'),
(21, 'Can add espacio', 6, 'add_espacio'),
(22, 'Can change espacio', 6, 'change_espacio'),
(23, 'Can delete espacio', 6, 'delete_espacio'),
(24, 'Can view espacio', 6, 'view_espacio'),
(25, 'Can add factura', 7, 'add_factura'),
(26, 'Can change factura', 7, 'change_factura'),
(27, 'Can delete factura', 7, 'delete_factura'),
(28, 'Can view factura', 7, 'view_factura'),
(29, 'Can add incidentes', 8, 'add_incidentes'),
(30, 'Can change incidentes', 8, 'change_incidentes'),
(31, 'Can delete incidentes', 8, 'delete_incidentes'),
(32, 'Can view incidentes', 8, 'view_incidentes'),
(33, 'Can add pagos alquileres', 9, 'add_pagosalquileres'),
(34, 'Can change pagos alquileres', 9, 'change_pagosalquileres'),
(35, 'Can delete pagos alquileres', 9, 'delete_pagosalquileres'),
(36, 'Can view pagos alquileres', 9, 'view_pagosalquileres'),
(37, 'Can add plan pagos', 10, 'add_planpagos'),
(38, 'Can change plan pagos', 10, 'change_planpagos'),
(39, 'Can delete plan pagos', 10, 'delete_planpagos'),
(40, 'Can view plan pagos', 10, 'view_planpagos'),
(41, 'Can add registro caja', 11, 'add_registrocaja'),
(42, 'Can change registro caja', 11, 'change_registrocaja'),
(43, 'Can delete registro caja', 11, 'delete_registrocaja'),
(44, 'Can view registro caja', 11, 'view_registrocaja'),
(45, 'Can add registro parqueo', 12, 'add_registroparqueo'),
(46, 'Can change registro parqueo', 12, 'change_registroparqueo'),
(47, 'Can delete registro parqueo', 12, 'delete_registroparqueo'),
(48, 'Can view registro parqueo', 12, 'view_registroparqueo'),
(49, 'Can add sector', 13, 'add_sector'),
(50, 'Can change sector', 13, 'change_sector'),
(51, 'Can delete sector', 13, 'delete_sector'),
(52, 'Can view sector', 13, 'view_sector'),
(53, 'Can add tarifa', 14, 'add_tarifa'),
(54, 'Can change tarifa', 14, 'change_tarifa'),
(55, 'Can delete tarifa', 14, 'delete_tarifa'),
(56, 'Can view tarifa', 14, 'view_tarifa'),
(57, 'Can add tarifa alquiler', 15, 'add_tarifaalquiler'),
(58, 'Can change tarifa alquiler', 15, 'change_tarifaalquiler'),
(59, 'Can delete tarifa alquiler', 15, 'delete_tarifaalquiler'),
(60, 'Can view tarifa alquiler', 15, 'view_tarifaalquiler'),
(61, 'Can add tipo espacio', 16, 'add_tipoespacio'),
(62, 'Can change tipo espacio', 16, 'change_tipoespacio'),
(63, 'Can delete tipo espacio', 16, 'delete_tipoespacio'),
(64, 'Can view tipo espacio', 16, 'view_tipoespacio'),
(65, 'Can add tipo usuario', 17, 'add_tipousuario'),
(66, 'Can change tipo usuario', 17, 'change_tipousuario'),
(67, 'Can delete tipo usuario', 17, 'delete_tipousuario'),
(68, 'Can view tipo usuario', 17, 'view_tipousuario'),
(69, 'Can add tipo vehiculo', 18, 'add_tipovehiculo'),
(70, 'Can change tipo vehiculo', 18, 'change_tipovehiculo'),
(71, 'Can delete tipo vehiculo', 18, 'delete_tipovehiculo'),
(72, 'Can view tipo vehiculo', 18, 'view_tipovehiculo'),
(73, 'Can add usuario', 19, 'add_usuario'),
(74, 'Can change usuario', 19, 'change_usuario'),
(75, 'Can delete usuario', 19, 'delete_usuario'),
(76, 'Can view usuario', 19, 'view_usuario'),
(77, 'Can add vehiculo', 20, 'add_vehiculo'),
(78, 'Can change vehiculo', 20, 'change_vehiculo'),
(79, 'Can delete vehiculo', 20, 'delete_vehiculo'),
(80, 'Can view vehiculo', 20, 'view_vehiculo'),
(81, 'Can add log entry', 21, 'add_logentry'),
(82, 'Can change log entry', 21, 'change_logentry'),
(83, 'Can delete log entry', 21, 'delete_logentry'),
(84, 'Can view log entry', 21, 'view_logentry'),
(85, 'Can add permission', 22, 'add_permission'),
(86, 'Can change permission', 22, 'change_permission'),
(87, 'Can delete permission', 22, 'delete_permission'),
(88, 'Can view permission', 22, 'view_permission'),
(89, 'Can add group', 23, 'add_group'),
(90, 'Can change group', 23, 'change_group'),
(91, 'Can delete group', 23, 'delete_group'),
(92, 'Can view group', 23, 'view_group'),
(93, 'Can add user', 24, 'add_user'),
(94, 'Can change user', 24, 'change_user'),
(95, 'Can delete user', 24, 'delete_user'),
(96, 'Can view user', 24, 'view_user'),
(97, 'Can add content type', 25, 'add_contenttype'),
(98, 'Can change content type', 25, 'change_contenttype'),
(99, 'Can delete content type', 25, 'delete_contenttype'),
(100, 'Can view content type', 25, 'view_contenttype'),
(101, 'Can add session', 26, 'add_session'),
(102, 'Can change session', 26, 'change_session'),
(103, 'Can delete session', 26, 'delete_session'),
(104, 'Can view session', 26, 'view_session'),
(105, 'Can add auth group', 27, 'add_authgroup'),
(106, 'Can change auth group', 27, 'change_authgroup'),
(107, 'Can delete auth group', 27, 'delete_authgroup'),
(108, 'Can view auth group', 27, 'view_authgroup'),
(109, 'Can add auth group permissions', 28, 'add_authgrouppermissions'),
(110, 'Can change auth group permissions', 28, 'change_authgrouppermissions'),
(111, 'Can delete auth group permissions', 28, 'delete_authgrouppermissions'),
(112, 'Can view auth group permissions', 28, 'view_authgrouppermissions'),
(113, 'Can add auth permission', 29, 'add_authpermission'),
(114, 'Can change auth permission', 29, 'change_authpermission'),
(115, 'Can delete auth permission', 29, 'delete_authpermission'),
(116, 'Can view auth permission', 29, 'view_authpermission'),
(117, 'Can add auth user', 30, 'add_authuser'),
(118, 'Can change auth user', 30, 'change_authuser'),
(119, 'Can delete auth user', 30, 'delete_authuser'),
(120, 'Can view auth user', 30, 'view_authuser'),
(121, 'Can add auth user groups', 31, 'add_authusergroups'),
(122, 'Can change auth user groups', 31, 'change_authusergroups'),
(123, 'Can delete auth user groups', 31, 'delete_authusergroups'),
(124, 'Can view auth user groups', 31, 'view_authusergroups'),
(125, 'Can add auth user user permissions', 32, 'add_authuseruserpermissions'),
(126, 'Can change auth user user permissions', 32, 'change_authuseruserpermissions'),
(127, 'Can delete auth user user permissions', 32, 'delete_authuseruserpermissions'),
(128, 'Can view auth user user permissions', 32, 'view_authuseruserpermissions'),
(129, 'Can add django admin log', 33, 'add_djangoadminlog'),
(130, 'Can change django admin log', 33, 'change_djangoadminlog'),
(131, 'Can delete django admin log', 33, 'delete_djangoadminlog'),
(132, 'Can view django admin log', 33, 'view_djangoadminlog'),
(133, 'Can add django content type', 34, 'add_djangocontenttype'),
(134, 'Can change django content type', 34, 'change_djangocontenttype'),
(135, 'Can delete django content type', 34, 'delete_djangocontenttype'),
(136, 'Can view django content type', 34, 'view_djangocontenttype'),
(137, 'Can add django migrations', 35, 'add_djangomigrations'),
(138, 'Can change django migrations', 35, 'change_djangomigrations'),
(139, 'Can delete django migrations', 35, 'delete_djangomigrations'),
(140, 'Can view django migrations', 35, 'view_djangomigrations'),
(141, 'Can add django session', 36, 'add_djangosession'),
(142, 'Can change django session', 36, 'change_djangosession'),
(143, 'Can delete django session', 36, 'delete_djangosession'),
(144, 'Can view django session', 36, 'view_djangosession');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `ci` varchar(30) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `ci`, `nombre`) VALUES
(1, '111', 'Chirstian Diaz'),
(2, '123', 'Marcelo Robledo'),
(3, '345', 'Maite Flores'),
(4, '123', 'Luis Revilla'),
(5, '413', 'Javier Recio'),
(6, '543-A', 'Claudia Arce'),
(7, '123-V', 'Pedro Escamoso'),
(8, '456-B', 'Ricardo Milos'),
(9, '789078675', 'Dario Benedetto'),
(10, '345-ASF', 'Diego La Torre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `control_horario`
--

CREATE TABLE `control_horario` (
  `id_control_horario` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `ingreso` time NOT NULL,
  `salida` time NOT NULL,
  `usuario_id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descuento`
--

CREATE TABLE `descuento` (
  `id_descuento` int(11) NOT NULL,
  `descripcion` text NOT NULL,
  `monto` double NOT NULL,
  `id_registro_parqueo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(21, 'admin', 'logentry'),
(23, 'auth', 'group'),
(22, 'auth', 'permission'),
(24, 'auth', 'user'),
(25, 'contenttypes', 'contenttype'),
(1, 'db', 'alquiler'),
(27, 'db', 'authgroup'),
(28, 'db', 'authgrouppermissions'),
(29, 'db', 'authpermission'),
(30, 'db', 'authuser'),
(31, 'db', 'authusergroups'),
(32, 'db', 'authuseruserpermissions'),
(2, 'db', 'cliente'),
(3, 'db', 'controlhorario'),
(4, 'db', 'descuento'),
(33, 'db', 'djangoadminlog'),
(34, 'db', 'djangocontenttype'),
(35, 'db', 'djangomigrations'),
(36, 'db', 'djangosession'),
(5, 'db', 'empresa'),
(6, 'db', 'espacio'),
(7, 'db', 'factura'),
(8, 'db', 'incidentes'),
(9, 'db', 'pagosalquileres'),
(10, 'db', 'planpagos'),
(11, 'db', 'registrocaja'),
(12, 'db', 'registroparqueo'),
(13, 'db', 'sector'),
(14, 'db', 'tarifa'),
(15, 'db', 'tarifaalquiler'),
(16, 'db', 'tipoespacio'),
(17, 'db', 'tipousuario'),
(18, 'db', 'tipovehiculo'),
(19, 'db', 'usuario'),
(20, 'db', 'vehiculo'),
(26, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-04 16:19:10.044699'),
(2, 'auth', '0001_initial', '2021-01-04 16:19:11.738916'),
(3, 'admin', '0001_initial', '2021-01-04 16:19:19.516854'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-04 16:19:21.149950'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-04 16:19:21.229565'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-04 16:19:22.065783'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-01-04 16:19:22.250826'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-01-04 16:19:22.457907'),
(9, 'auth', '0004_alter_user_username_opts', '2021-01-04 16:19:22.524614'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-01-04 16:19:23.231040'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-01-04 16:19:23.285540'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-01-04 16:19:23.353599'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-01-04 16:19:23.581830'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-01-04 16:19:23.951676'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-01-04 16:19:24.139159'),
(16, 'auth', '0011_update_proxy_permissions', '2021-01-04 16:19:24.191770'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-01-04 16:19:24.337373'),
(18, 'db', '0001_initial', '2021-01-04 16:19:24.408249'),
(19, 'sessions', '0001_initial', '2021-01-04 16:19:24.797959'),
(20, 'db', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django', '2021-01-04 16:23:30.139584');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id_empresa` int(11) NOT NULL,
  `nit` varchar(45) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `razon_social` varchar(40) NOT NULL,
  `direccion` text NOT NULL,
  `contacto` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `espacio`
--

CREATE TABLE `espacio` (
  `id_espacio` int(11) NOT NULL,
  `posicion` varchar(20) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `id_sector` int(11) NOT NULL,
  `tipo_espacio_id_tipo_espacio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL,
  `codigo_control` varchar(30) NOT NULL,
  `autorizacion` int(11) NOT NULL,
  `empresa_id_empresa` int(11) NOT NULL,
  `alquiler_id_alquiler` int(11) NOT NULL,
  `registro_parqueo_id_parqueo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `incidentes`
--

CREATE TABLE `incidentes` (
  `id_incidentes` int(11) NOT NULL,
  `descripcion` text NOT NULL,
  `id_registro_parqueo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos_alquileres`
--

CREATE TABLE `pagos_alquileres` (
  `id_pago_cuotas` int(11) NOT NULL,
  `nro_cuota` int(11) NOT NULL,
  `estado_cuota` varchar(20) NOT NULL,
  `fecha` datetime NOT NULL,
  `plan_pagos_id_plan_de_pagos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `pagos_alquileres`
--

INSERT INTO `pagos_alquileres` (`id_pago_cuotas`, `nro_cuota`, `estado_cuota`, `fecha`, `plan_pagos_id_plan_de_pagos`) VALUES
(1, 1, 'PAGADO', '2019-02-08 00:00:00', 1),
(2, 2, 'PAGADO', '2019-03-08 00:00:00', 1),
(3, 3, 'EN DEUDA', '2019-04-08 00:00:00', 1),
(4, 1, 'PAGADO', '2019-02-08 00:00:00', 2),
(5, 2, 'PAGADO', '2019-03-08 00:00:00', 2),
(6, 3, 'PAGADO', '2019-04-08 00:00:00', 2),
(7, 4, 'PAGADO', '2019-05-08 00:00:00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plan_pagos`
--

CREATE TABLE `plan_pagos` (
  `id_plan_de_pagos` int(11) NOT NULL,
  `monto_cuota` double NOT NULL,
  `num_cuotas` int(11) NOT NULL,
  `alquiler_id_alquiler` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `plan_pagos`
--

INSERT INTO `plan_pagos` (`id_plan_de_pagos`, `monto_cuota`, `num_cuotas`, `alquiler_id_alquiler`) VALUES
(1, 33.33, 3, 1),
(2, 100, 4, 2),
(3, 200, 5, 3),
(4, 100, 2, 4),
(5, 20, 3, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_caja`
--

CREATE TABLE `registro_caja` (
  `id_registro_caja` int(11) NOT NULL,
  `hora_apertura` time NOT NULL,
  `hora_clausura` time DEFAULT NULL,
  `monto_apertura` double NOT NULL,
  `monto_clausura` double DEFAULT NULL,
  `estado` varchar(40) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `registro_caja`
--

INSERT INTO `registro_caja` (`id_registro_caja`, `hora_apertura`, `hora_clausura`, `monto_apertura`, `monto_clausura`, `estado`, `id_usuario`, `fecha`) VALUES
(1, '07:30:00', '22:01:06', 200, 150, 'CERRADO', 2, '2021-01-04'),
(2, '07:30:00', '22:01:06', 300, 300, 'CERRADO', 3, '2021-01-05'),
(3, '07:30:00', '22:01:06', 300, 290, 'CERRADO', 2, '2021-01-06'),
(4, '07:30:00', '22:33:16', 200, 150, 'CERRADO', 3, '2021-01-07'),
(5, '07:30:00', '22:33:16', 200, 150, 'CERRADO', 2, '2020-12-20'),
(6, '07:30:00', '22:33:16', 300, 300, 'CERRADO', 2, '2020-12-21'),
(7, '07:30:00', '22:33:16', 300, 300, 'CERRADO', 2, '2020-12-22'),
(8, '07:30:00', '22:33:16', 300, 300, 'CERRADO', 3, '2020-12-23'),
(9, '07:30:00', '22:33:16', 300, 300, 'CERRADO', 3, '2020-12-24'),
(10, '07:30:00', '22:33:16', 300, 300, 'CERRADO', 3, '2020-12-25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_parqueo`
--

CREATE TABLE `registro_parqueo` (
  `id_parqueo` int(11) NOT NULL,
  `entrada` datetime NOT NULL,
  `salida` datetime NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `vehiculo_id` int(11) NOT NULL,
  `id_espacio` int(11) NOT NULL,
  `id_tarifas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sector`
--

CREATE TABLE `sector` (
  `id_sector` int(11) NOT NULL,
  `sector` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarifa`
--

CREATE TABLE `tarifa` (
  `id_tarifas` int(11) NOT NULL,
  `horas` int(11) NOT NULL,
  `dias` int(11) NOT NULL,
  `precio` double(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tarifa`
--

INSERT INTO `tarifa` (`id_tarifas`, `horas`, `dias`, `precio`) VALUES
(1, 1, 0, 4.00),
(2, 2, 0, 10.00),
(3, 3, 0, 15.00),
(4, 4, 0, 20.00),
(5, 5, 0, 25.00),
(6, 6, 0, 28.00),
(7, 3, 3, 87.00),
(8, 6, 3, 200.00),
(9, 4, 5, 341.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tarifa_alquiler`
--

CREATE TABLE `tarifa_alquiler` (
  `id_tarifa_alquiler` int(11) NOT NULL,
  `meses` int(11) NOT NULL,
  `precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tarifa_alquiler`
--

INSERT INTO `tarifa_alquiler` (`id_tarifa_alquiler`, `meses`, `precio`) VALUES
(1, 4, 200),
(2, 2, 100),
(3, 3, 300),
(4, 5, 200),
(5, 6, 1000),
(6, 1, 44);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_espacio`
--

CREATE TABLE `tipo_espacio` (
  `id_tipo_espacio` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id_tipo_usuario` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id_tipo_usuario`, `tipo`) VALUES
(1, 'ADMINISTRADOR'),
(2, 'EMPLEADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_vehiculo`
--

CREATE TABLE `tipo_vehiculo` (
  `id_tipo_vehiculo` int(11) NOT NULL,
  `tipo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_vehiculo`
--

INSERT INTO `tipo_vehiculo` (`id_tipo_vehiculo`, `tipo`) VALUES
(1, 'Automovil'),
(2, 'Motocicleta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `ci` varchar(30) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `hora_ingreso` time DEFAULT NULL,
  `hora_salida` time DEFAULT NULL,
  `id_tipo_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `ci`, `nombre`, `usuario`, `password`, `hora_ingreso`, `hora_salida`, `id_tipo_usuario`) VALUES
(1, '3290765', 'Walter Flores', 'waltico', '12345', NULL, NULL, 1),
(2, '5678212', 'Javier Rojas', 'javi_roj', '12345', '07:30:00', '22:30:00', 2),
(3, '9802134', 'Roberto Carlo Fernandez', 'rcf', '12345', '07:30:00', '22:30:00', 2),
(4, '123', 'Adrian Jusino', 'jusi', '123', '07:30:00', '22:30:00', 2),
(5, '12345', 'Erwin Saavedra', 'erwin', '123', '07:30:00', '22:30:00', 2),
(6, '213456', 'Juan Cataldi', 'juca', '123', '06:30:00', '22:30:00', 2),
(7, '213e4r', 'Roberto Dominguez', 'rodo', '123', '07:30:00', '22:30:00', 2),
(8, '1234', 'Diego Bejarano', 'dibe', '123', '07:30:00', '22:30:00', 2),
(9, '456', 'Roberto Galindo', 'rogaw', '1234', '07:30:00', '22:30:00', 2),
(10, '123', 'Kevin Farrell', 'keva', '123', '07:30:00', '22:30:00', 2),
(11, '234r5tgfvd', 'Pablo Escobar', 'paes', '123', '07:30:00', '22:30:00', 2),
(12, 'eqws', 'Daniel Nosiglia', 'danosiglia', '123', '07:30:00', '22:30:00', 2),
(13, '543-A', 'Pedro Azogue', 'pedrito_de_cristal', '123', '07:30:00', '22:30:00', 2),
(14, '123-B', 'Marcelo Martins', 'mars', '1234', '07:30:00', '22:30:00', 2),
(15, '45678-U', 'Rodrigo Ramallo', 'rorama', '123', '11:57:00', '09:59:00', 2),
(16, '45678-F', 'Tacuara Cardozo', 'tacucard', '123', '14:00:00', '11:06:00', 2),
(17, '123-B', 'Ronaldo Sanchez', 'ronasanch', '1234', '11:07:00', '17:01:00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE `vehiculo` (
  `id_vehiculo` int(11) NOT NULL,
  `placa` varchar(30) NOT NULL,
  `marca_modelo` varchar(45) DEFAULT NULL,
  `color` varchar(15) NOT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `tipo_vehiculo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `vehiculo`
--

INSERT INTO `vehiculo` (`id_vehiculo`, `placa`, `marca_modelo`, `color`, `cliente_id`, `tipo_vehiculo_id`) VALUES
(1, 'ABC-123', 'Nissan Gran Vitarra', 'Verde', 1, 1),
(2, 'FRD-125', 'Toyota Corolla', 'Blanco', 2, 1),
(3, 'GTF-765', 'Ford Focus', 'Amarillo', 8, 1),
(4, 'FRD-123', 'Mazda G', 'Rojo', 4, 1),
(5, 'SDA-645', 'Honda Revolution', 'Verde', 7, 2),
(6, 'GTM-642', 'Mercedes SL600', 'Blanco', 3, 1),
(7, 'FRE-123', 'BMW 65', 'Amarillo', 1, 1),
(8, 'DES-653', 'Volkswagen Peta', 'Rojo', 6, 1),
(9, 'FRE-124', 'Honda Modelo H', 'Verde', 10, 2),
(10, 'DES-654', 'Honda Modelo S', 'Azul', 5, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD PRIMARY KEY (`id_alquiler`),
  ADD KEY `alquiler_cliente` (`cliente_id_cliente`),
  ADD KEY `alquiler_tarifa_alquiler` (`id_tarifa_alquiler`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `control_horario`
--
ALTER TABLE `control_horario`
  ADD PRIMARY KEY (`id_control_horario`),
  ADD KEY `control_horario_usuario` (`usuario_id_usuario`);

--
-- Indices de la tabla `descuento`
--
ALTER TABLE `descuento`
  ADD PRIMARY KEY (`id_descuento`),
  ADD KEY `descuento_registro_parqueo` (`id_registro_parqueo`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id_empresa`);

--
-- Indices de la tabla `espacio`
--
ALTER TABLE `espacio`
  ADD PRIMARY KEY (`id_espacio`),
  ADD KEY `espacio_sector` (`id_sector`),
  ADD KEY `espacio_tipo_espacio` (`tipo_espacio_id_tipo_espacio`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id_factura`),
  ADD KEY `factura_alquiler` (`alquiler_id_alquiler`),
  ADD KEY `factura_empresa` (`empresa_id_empresa`),
  ADD KEY `factura_registro_parqueo` (`registro_parqueo_id_parqueo`);

--
-- Indices de la tabla `incidentes`
--
ALTER TABLE `incidentes`
  ADD PRIMARY KEY (`id_incidentes`),
  ADD KEY `incidentes_registro_parqueo` (`id_registro_parqueo`);

--
-- Indices de la tabla `pagos_alquileres`
--
ALTER TABLE `pagos_alquileres`
  ADD PRIMARY KEY (`id_pago_cuotas`),
  ADD KEY `pagos_alquileres_plan_pagos` (`plan_pagos_id_plan_de_pagos`);

--
-- Indices de la tabla `plan_pagos`
--
ALTER TABLE `plan_pagos`
  ADD PRIMARY KEY (`id_plan_de_pagos`),
  ADD KEY `plan_pagos_alquiler` (`alquiler_id_alquiler`);

--
-- Indices de la tabla `registro_caja`
--
ALTER TABLE `registro_caja`
  ADD PRIMARY KEY (`id_registro_caja`),
  ADD KEY `registro_caja_usuario` (`id_usuario`);

--
-- Indices de la tabla `registro_parqueo`
--
ALTER TABLE `registro_parqueo`
  ADD PRIMARY KEY (`id_parqueo`),
  ADD KEY `registro_parqueo_espacio` (`id_espacio`),
  ADD KEY `registro_parqueo_tarifa` (`id_tarifas`),
  ADD KEY `registro_parqueo_usuario` (`id_usuario`),
  ADD KEY `registro_parqueo_vehiculo` (`vehiculo_id`);

--
-- Indices de la tabla `sector`
--
ALTER TABLE `sector`
  ADD PRIMARY KEY (`id_sector`);

--
-- Indices de la tabla `tarifa`
--
ALTER TABLE `tarifa`
  ADD PRIMARY KEY (`id_tarifas`);

--
-- Indices de la tabla `tarifa_alquiler`
--
ALTER TABLE `tarifa_alquiler`
  ADD PRIMARY KEY (`id_tarifa_alquiler`);

--
-- Indices de la tabla `tipo_espacio`
--
ALTER TABLE `tipo_espacio`
  ADD PRIMARY KEY (`id_tipo_espacio`);

--
-- Indices de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id_tipo_usuario`);

--
-- Indices de la tabla `tipo_vehiculo`
--
ALTER TABLE `tipo_vehiculo`
  ADD PRIMARY KEY (`id_tipo_vehiculo`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `usuario_tipo_usuario` (`id_tipo_usuario`);

--
-- Indices de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD PRIMARY KEY (`id_vehiculo`),
  ADD KEY `vehiculo_cliente` (`cliente_id`),
  ADD KEY `vehiculo_tipo_vehiculo` (`tipo_vehiculo_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alquiler`
--
ALTER TABLE `alquiler`
  MODIFY `id_alquiler` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=145;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `control_horario`
--
ALTER TABLE `control_horario`
  MODIFY `id_control_horario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `descuento`
--
ALTER TABLE `descuento`
  MODIFY `id_descuento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id_empresa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `espacio`
--
ALTER TABLE `espacio`
  MODIFY `id_espacio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `incidentes`
--
ALTER TABLE `incidentes`
  MODIFY `id_incidentes` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pagos_alquileres`
--
ALTER TABLE `pagos_alquileres`
  MODIFY `id_pago_cuotas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `plan_pagos`
--
ALTER TABLE `plan_pagos`
  MODIFY `id_plan_de_pagos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `registro_caja`
--
ALTER TABLE `registro_caja`
  MODIFY `id_registro_caja` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `registro_parqueo`
--
ALTER TABLE `registro_parqueo`
  MODIFY `id_parqueo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tarifa`
--
ALTER TABLE `tarifa`
  MODIFY `id_tarifas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tarifa_alquiler`
--
ALTER TABLE `tarifa_alquiler`
  MODIFY `id_tarifa_alquiler` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tipo_espacio`
--
ALTER TABLE `tipo_espacio`
  MODIFY `id_tipo_espacio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  MODIFY `id_tipo_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_vehiculo`
--
ALTER TABLE `tipo_vehiculo`
  MODIFY `id_tipo_vehiculo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  MODIFY `id_vehiculo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alquiler`
--
ALTER TABLE `alquiler`
  ADD CONSTRAINT `alquiler_cliente` FOREIGN KEY (`cliente_id_cliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `alquiler_tarifa_alquiler` FOREIGN KEY (`id_tarifa_alquiler`) REFERENCES `tarifa_alquiler` (`id_tarifa_alquiler`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `control_horario`
--
ALTER TABLE `control_horario`
  ADD CONSTRAINT `control_horario_usuario` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `descuento`
--
ALTER TABLE `descuento`
  ADD CONSTRAINT `descuento_registro_parqueo` FOREIGN KEY (`id_registro_parqueo`) REFERENCES `registro_parqueo` (`id_parqueo`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `espacio`
--
ALTER TABLE `espacio`
  ADD CONSTRAINT `espacio_sector` FOREIGN KEY (`id_sector`) REFERENCES `sector` (`id_sector`),
  ADD CONSTRAINT `espacio_tipo_espacio` FOREIGN KEY (`tipo_espacio_id_tipo_espacio`) REFERENCES `tipo_espacio` (`id_tipo_espacio`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_alquiler` FOREIGN KEY (`alquiler_id_alquiler`) REFERENCES `alquiler` (`id_alquiler`),
  ADD CONSTRAINT `factura_empresa` FOREIGN KEY (`empresa_id_empresa`) REFERENCES `empresa` (`id_empresa`),
  ADD CONSTRAINT `factura_registro_parqueo` FOREIGN KEY (`registro_parqueo_id_parqueo`) REFERENCES `registro_parqueo` (`id_parqueo`);

--
-- Filtros para la tabla `incidentes`
--
ALTER TABLE `incidentes`
  ADD CONSTRAINT `incidentes_registro_parqueo` FOREIGN KEY (`id_registro_parqueo`) REFERENCES `registro_parqueo` (`id_parqueo`);

--
-- Filtros para la tabla `pagos_alquileres`
--
ALTER TABLE `pagos_alquileres`
  ADD CONSTRAINT `pagos_alquileres_plan_pagos` FOREIGN KEY (`plan_pagos_id_plan_de_pagos`) REFERENCES `plan_pagos` (`id_plan_de_pagos`);

--
-- Filtros para la tabla `plan_pagos`
--
ALTER TABLE `plan_pagos`
  ADD CONSTRAINT `plan_pagos_alquiler` FOREIGN KEY (`alquiler_id_alquiler`) REFERENCES `alquiler` (`id_alquiler`);

--
-- Filtros para la tabla `registro_caja`
--
ALTER TABLE `registro_caja`
  ADD CONSTRAINT `registro_caja_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `registro_parqueo`
--
ALTER TABLE `registro_parqueo`
  ADD CONSTRAINT `registro_parqueo_espacio` FOREIGN KEY (`id_espacio`) REFERENCES `espacio` (`id_espacio`),
  ADD CONSTRAINT `registro_parqueo_tarifa` FOREIGN KEY (`id_tarifas`) REFERENCES `tarifa` (`id_tarifas`),
  ADD CONSTRAINT `registro_parqueo_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  ADD CONSTRAINT `registro_parqueo_vehiculo` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo` (`id_vehiculo`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_tipo_usuario` FOREIGN KEY (`id_tipo_usuario`) REFERENCES `tipo_usuario` (`id_tipo_usuario`);

--
-- Filtros para la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD CONSTRAINT `vehiculo_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `vehiculo_tipo_vehiculo` FOREIGN KEY (`tipo_vehiculo_id`) REFERENCES `tipo_vehiculo` (`id_tipo_vehiculo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
