 
-- ---------------------------------------------------------------------
-- EMPRESAS
-- ---------------------------------------------------------------------
INSERT INTO EMPRESA (id, nombre_empresa, fecha_registro, estado) VALUES
(1, 'Constructora XYZ', '2024-01-15 08:00:00', '1'),
(2, 'Mantenimiento Industrial Andes', '2024-02-10 09:30:00', '1'),
(3, 'Logística Rápida del Valle', '2024-03-05 10:15:00', '1');
 
-- ---------------------------------------------------------------------
-- USUARIOS
-- 1 admin_empresa + 2 coordinadores + 7 tecnicos por empresa = 10 c/u
-- contraseña de prueba para todos: "1234" (texto plano, version de prueba)
-- ---------------------------------------------------------------------
 
-- Empresa 1: Constructora XYZ (ids 1-10)
INSERT INTO USUARIO (id, nombre, correo, contraseña, rol, area, cargo, empresa_id) VALUES
(1,  'Ana Torres',       'ana.torres@xyz.com',       '1234', 'admin_empresa', 'Gerencia',        'Administradora General', 1),
(2,  'Jorge Ramírez',    'jorge.ramirez@xyz.com',    '1234', 'coordinador',   'Obras',           'Coordinador de Obras',   1),
(3,  'Patricia Gómez',   'patricia.gomez@xyz.com',   '1234', 'coordinador',   'Mantenimiento',   'Coordinadora',           1),
(4,  'Pedro García',     'pedro.garcia@xyz.com',     '1234', 'tecnico',       'Obras',           'Técnico Albañil',        1),
(5,  'Luis Martínez',    'luis.martinez@xyz.com',    '1234', 'tecnico',       'Obras',           'Técnico Electricista',   1),
(6,  'Carmen Ruiz',      'carmen.ruiz@xyz.com',      '1234', 'tecnico',       'Obras',           'Técnica Plomería',       1),
(7,  'Diego Salazar',    'diego.salazar@xyz.com',    '1234', 'tecnico',       'Mantenimiento',   'Técnico General',        1),
(8,  'Mónica Pardo',     'monica.pardo@xyz.com',     '1234', 'tecnico',       'Mantenimiento',   'Técnica Pintura',        1),
(9,  'Felipe Castro',    'felipe.castro@xyz.com',    '1234', 'tecnico',       'Obras',           'Técnico Soldador',       1),
(10, 'Valentina Rojas',  'valentina.rojas@xyz.com',  '1234', 'tecnico',       'Obras',           'Técnica Auxiliar',       1);
 
-- Empresa 2: Mantenimiento Industrial Andes (ids 11-20)
INSERT INTO USUARIO (id, nombre, correo, contraseña, rol, area, cargo, empresa_id) VALUES
(11, 'Roberto Vega',     'roberto.vega@andes.com',    '1234', 'admin_empresa', 'Gerencia',        'Administrador General',  2),
(12, 'Claudia Herrera',  'claudia.herrera@andes.com', '1234', 'coordinador',   'Planta',          'Coordinadora de Planta', 2),
(13, 'Andrés Morales',   'andres.morales@andes.com',  '1234', 'coordinador',   'Campo',           'Coordinador de Campo',   2),
(14, 'Sandra Quintero',  'sandra.quintero@andes.com', '1234', 'tecnico',       'Planta',          'Técnica Eléctrica',      2),
(15, 'Hernán Vargas',    'hernan.vargas@andes.com',   '1234', 'tecnico',       'Planta',          'Técnico Mecánico',       2),
(16, 'Liliana Cárdenas', 'liliana.cardenas@andes.com','1234', 'tecnico',       'Campo',           'Técnica Instrumentación',2),
(17, 'Camilo Restrepo',  'camilo.restrepo@andes.com', '1234', 'tecnico',       'Campo',           'Técnico de Campo',       2),
(18, 'Natalia Ospina',   'natalia.ospina@andes.com',  '1234', 'tecnico',       'Planta',          'Técnica de Calidad',     2),
(19, 'Sergio Londoño',   'sergio.londono@andes.com',  '1234', 'tecnico',       'Campo',           'Técnico Hidráulico',     2),
(20, 'Paula Mejía',      'paula.mejia@andes.com',     '1234', 'tecnico',       'Planta',          'Técnica Auxiliar',       2);
 
-- Empresa 3: Logística Rápida del Valle (ids 21-30)
INSERT INTO USUARIO (id, nombre, correo, contraseña, rol, area, cargo, empresa_id) VALUES
(21, 'Mauricio Idárraga','mauricio.idarraga@valle.com','1234','admin_empresa', 'Gerencia',        'Administrador General',  3),
(22, 'Lorena Zapata',    'lorena.zapata@valle.com',    '1234', 'coordinador',  'Bodega',          'Coordinadora de Bodega', 3),
(23, 'Esteban Correa',   'esteban.correa@valle.com',   '1234', 'coordinador',  'Transporte',      'Coordinador de Flota',  3),
(24, 'Tatiana Bermúdez', 'tatiana.bermudez@valle.com', '1234', 'tecnico',      'Bodega',          'Técnica de Inventario', 3),
(25, 'Ricardo Peña',     'ricardo.pena@valle.com',     '1234', 'tecnico',      'Transporte',      'Técnico de Flota',      3),
(26, 'Daniela Suárez',   'daniela.suarez@valle.com',   '1234', 'tecnico',      'Bodega',          'Técnica de Empaque',    3),
(27, 'Iván Beltrán',     'ivan.beltran@valle.com',     '1234', 'tecnico',      'Transporte',      'Técnico Mecánico',      3),
(28, 'Carolina Duarte',  'carolina.duarte@valle.com',  '1234', 'tecnico',      'Bodega',          'Técnica Auxiliar',      3),
(29, 'Julián Pacheco',   'julian.pacheco@valle.com',   '1234', 'tecnico',      'Transporte',      'Técnico Conductor',     3),
(30, 'Gabriela Niño',    'gabriela.nino@valle.com',    '1234', 'tecnico',      'Bodega',          'Técnica de Calidad',    3);
 
-- ---------------------------------------------------------------------
-- TAREAS
-- Creadas por coordinadores de cada empresa
-- ---------------------------------------------------------------------
 
-- Empresa 1: Constructora XYZ
INSERT INTO TAREA (id, titulo, descripcion, prioridad, fecha_limite, ubicacion, estado, fecha_creacion, coordinador_id, empresa_id) VALUES
(1, 'Reparar techo edificio A',        'Filtración de agua en el techo del bloque A, requiere impermeabilización.', 'alta',  '2026-06-25 17:00:00', 'Edificio A - Piso 5',     '2', '2026-06-10 08:30:00', 2, 1),
(2, 'Instalación eléctrica torre 2',   'Cableado e instalación de tableros eléctricos en la torre 2.',             'alta',  '2026-07-01 17:00:00', 'Torre 2 - Subestación',   '1',  '2026-06-12 09:00:00', 2, 1),
(3, 'Mantenimiento de plomería bloque B','Revisión y cambio de tuberías con fugas reportadas.',                    'media', '2026-06-30 17:00:00', 'Bloque B - Piso 2',       '1',  '2026-06-13 10:15:00', 3, 1),
(4, 'Pintura fachada principal',       'Pintura exterior completa de la fachada principal del proyecto.',          'baja',  '2026-07-15 17:00:00', 'Fachada principal',       '1',  '2026-06-14 11:00:00', 3, 1);
 
-- Empresa 2: Mantenimiento Industrial Andes
INSERT INTO TAREA (id, titulo, descripcion, prioridad, fecha_limite, ubicacion, estado, fecha_creacion, coordinador_id, empresa_id) VALUES
(5, 'Revisión motor línea 3',          'Inspección y mantenimiento preventivo del motor de la línea de producción 3.', 'alta',  '2026-06-22 17:00:00', 'Planta - Línea 3',        '2', '2026-06-09 07:45:00', 12, 2),
(6, 'Calibración de instrumentos',     'Calibración de sensores de presión y temperatura en planta.',                 'media', '2026-06-28 17:00:00', 'Planta - Sala de control','1',  '2026-06-11 08:20:00', 12, 2),
(7, 'Reparación sistema hidráulico',   'Fuga detectada en el sistema hidráulico de la prensa principal.',             'alta',  '2026-06-24 17:00:00', 'Planta - Zona de prensas','2', '2026-06-12 13:00:00', 13, 2);
 
-- Empresa 3: Logística Rápida del Valle
INSERT INTO TAREA (id, titulo, descripcion, prioridad, fecha_limite, ubicacion, estado, fecha_creacion, coordinador_id, empresa_id) VALUES
(8, 'Mantenimiento flota vehículo 12', 'Cambio de aceite, frenos y revisión general del vehículo de reparto 12.', 'media', '2026-06-26 17:00:00', 'Patio de flota',          '1',  '2026-06-10 14:00:00', 23, 3),
(9, 'Reorganización de bodega central','Reordenamiento de inventario y etiquetado de estanterías.',               'baja',  '2026-07-05 17:00:00', 'Bodega central',          '1',  '2026-06-13 09:30:00', 22, 3),
(10,'Reparación montacargas',          'El montacargas 02 presenta falla en el sistema de elevación.',            'alta',  '2026-06-23 17:00:00', 'Bodega central - Andén 2','2', '2026-06-14 08:00:00', 22, 3);
 
-- ---------------------------------------------------------------------
-- ASIGNACION_TAREA
-- Cada tarea con 2-3 técnicos de su misma empresa, uno marcado lider
-- ---------------------------------------------------------------------
 
-- Tarea 1: Reparar techo edificio A (XYZ) -> Pedro lider, Carmen
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(1, 4, 1),
(1, 6, 0);
 
-- Tarea 2: Instalación eléctrica torre 2 (XYZ) -> Luis lider, Felipe
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(2, 5, 1),
(2, 9, 0);
 
-- Tarea 3: Mantenimiento plomería bloque B (XYZ) -> Carmen lider, Valentina, Diego
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(3, 6, 1),
(3, 10, 0),
(3, 7, 0);
 
-- Tarea 4: Pintura fachada principal (XYZ) -> Mónica lider
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(4, 8, 1);
 
-- Tarea 5: Revisión motor línea 3 (Andes) -> Hernán lider, Sandra
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(5, 15, 1),
(5, 14, 0);
 
-- Tarea 6: Calibración de instrumentos (Andes) -> Liliana lider, Natalia
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(6, 16, 1),
(6, 18, 0);
 
-- Tarea 7: Reparación sistema hidráulico (Andes) -> Sergio lider, Camilo, Paula
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(7, 19, 1),
(7, 17, 0),
(7, 20, 0);
 
-- Tarea 8: Mantenimiento flota vehículo 12 (Valle) -> Ricardo lider, Iván
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(8, 25, 1),
(8, 27, 0);
 
-- Tarea 9: Reorganización bodega central (Valle) -> Daniela lider, Carolina
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(9, 26, 1),
(9, 28, 0);
 
-- Tarea 10: Reparación montacargas (Valle) -> Julián lider, Tatiana, Gabriela
INSERT INTO ASIGNACION_TAREA (tarea_id, tecnico_id, es_lider) VALUES
(10, 29, 1),
(10, 24, 0),
(10, 30, 0);
 
-- ---------------------------------------------------------------------
-- EVIDENCIA
-- Solo subidas por el tecnico lider de cada tarea
-- ---------------------------------------------------------------------
INSERT INTO EVIDENCIA (id, tarea_id, tecnico_id, ruta_archivo, tipo_archivo, comentario, fecha_subida) VALUES
(1, 1, 4,  '/evidencias/tarea1_foto_filtracion.jpg',  'imagen', 'Foto de la zona afectada antes de iniciar la reparación.', '2026-06-11 09:00:00'),
(2, 1, 4,  '/evidencias/tarea1_avance_membrana.jpg',  'imagen', 'Avance de instalación de membrana impermeabilizante.',     '2026-06-13 16:30:00'),
(3, 2, 5,  '/evidencias/tarea2_plano_electrico.pdf',  'documento', 'Plano eléctrico actualizado de la torre 2.',             '2026-06-12 10:00:00'),
(4, 3, 6,  '/evidencias/tarea3_tuberia_dañada.jpg',   'imagen', 'Tramo de tubería con fuga identificada.',                 '2026-06-13 11:45:00'),
(5, 5, 15, '/evidencias/tarea5_motor_inspeccion.jpg', 'imagen', 'Estado del motor antes del mantenimiento preventivo.',    '2026-06-10 08:00:00'),
(6, 7, 19, '/evidencias/tarea7_fuga_hidraulica.mp4',  'video',  'Video mostrando la fuga en el sistema hidráulico.',       '2026-06-13 14:20:00'),
(7, 8, 25, '/evidencias/tarea8_estado_frenos.jpg',    'imagen', 'Estado de las pastillas de freno antes del cambio.',      '2026-06-11 09:30:00'),
(8, 10, 29,'/evidencias/tarea10_falla_elevacion.jpg', 'imagen', 'Falla detectada en el sistema de elevación del montacargas.', '2026-06-14 10:10:00');
 
-- ---------------------------------------------------------------------
-- SOLICITUD_INSUMO
-- Solo solicitadas por el tecnico lider de cada tarea
-- ---------------------------------------------------------------------
INSERT INTO SOLICITUD_INSUMO (id, tarea_id, tecnico_id, nombre_material, cantidad, justificacion, estado, fecha_solicitud) VALUES
(1, 1, 4,  'Membrana impermeabilizante', 10, 'Se requiere para cubrir la zona de filtración del techo.',        '2',  '2026-06-11 09:15:00'),
(2, 1, 4,  'Sellador asfáltico',          5, 'Sellado de juntas posteriores a la instalación de la membrana.',   '1', '2026-06-13 16:45:00'),
(3, 2, 5,  'Cable eléctrico calibre 12', 50, 'Cableado del nuevo tablero de la torre 2.',                        '2',  '2026-06-12 10:30:00'),
(4, 3, 6,  'Tubería PVC 1/2 pulgada',    20, 'Reemplazo del tramo de tubería con fuga.',                         '1', '2026-06-13 12:00:00'),
(5, 5, 15, 'Aceite lubricante industrial',8, 'Cambio de aceite como parte del mantenimiento preventivo.',        '2',  '2026-06-10 08:15:00'),
(6, 7, 19, 'Manguera hidráulica de alta presión', 3, 'Reemplazo de la manguera que presenta la fuga.',           '3', '2026-06-13 14:40:00'),
(7, 8, 25, 'Pastillas de freno',          4, 'Cambio programado de pastillas de freno del vehículo 12.',         '2',  '2026-06-11 09:45:00'),
(8, 10, 29,'Cadena de elevación',         1, 'Reemplazo de la cadena de elevación dañada del montacargas.',      '1', '2026-06-14 10:25:00');
 
-- ---------------------------------------------------------------------
-- REGISTRO_ACTIVIDAD
-- Cualquier tecnico asignado (lider o no) puede registrar actividad
-- ---------------------------------------------------------------------
INSERT INTO REGISTRO_ACTIVIDAD (id, tarea_id, usuario_id, accion, fecha) VALUES
(1,  1, 4,  'Inicio de inspección de la zona afectada por filtración.',           '2026-06-11 08:30:00'),
(2,  1, 6,  'Apoyo en limpieza de la superficie antes de impermeabilizar.',       '2026-06-12 09:00:00'),
(3,  1, 4,  'Aplicación de primera capa de membrana impermeabilizante.',          '2026-06-13 15:00:00'),
(4,  2, 5,  'Revisión de plano eléctrico y verificación de materiales.',          '2026-06-12 09:30:00'),
(5,  3, 6,  'Identificación del tramo de tubería con fuga.',                     '2026-06-13 11:00:00'),
(6,  3, 10, 'Apoyo en corte de tubería dañada.',                                 '2026-06-13 11:30:00'),
(7,  5, 15, 'Inicio de inspección del motor de la línea 3.',                     '2026-06-10 07:50:00'),
(8,  5, 14, 'Registro de parámetros de temperatura y vibración del motor.',      '2026-06-10 08:30:00'),
(9,  7, 19, 'Detección de fuga en manguera hidráulica de la prensa.',            '2026-06-13 13:30:00'),
(10, 7, 17, 'Apoyo en aislamiento del sistema antes de la reparación.',          '2026-06-13 14:00:00'),
(11, 8, 25, 'Inspección de frenos y niveles de aceite del vehículo 12.',         '2026-06-11 09:00:00'),
(12, 10,29, 'Diagnóstico de falla en el sistema de elevación del montacargas.', '2026-06-14 09:00:00'),
(13, 10,24, 'Apoyo en verificación de cadena y poleas del montacargas.',        '2026-06-14 09:40:00');
 