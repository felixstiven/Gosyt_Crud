USE gosyt_db;

-- Tabla EMPRESA
CREATE TABLE IF NOT EXISTS EMPRESA (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(100) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('activa', 'inactiva') DEFAULT 'activa'
);

-- Tabla USUARIO (Unifica Admin, Coordinador y Tecnico)
CREATE TABLE IF NOT EXISTS USUARIO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol ENUM('admin_empresa', 'coordinador', 'tecnico') NOT NULL,
    area VARCHAR(50), -- mantenimiento | construccion
    cargo VARCHAR(50), -- Jefe | Administrativo | Calidad
    empresa_id INT,
    FOREIGN KEY (empresa_id) REFERENCES EMPRESA(id) ON DELETE CASCADE
);

-- Tabla TAREA
CREATE TABLE IF NOT EXISTS TAREA (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    prioridad ENUM('alta', 'media', 'baja') DEFAULT 'media',
    fecha_limite DATETIME,
    ubicacion VARCHAR(150),
    estado ENUM('pendiente', 'en_proceso', 'completada', 'retrasada') DEFAULT 'pendiente',
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    -- Referencia al coordinador que la creó
    coordinador_id INT,
    -- Referencia histórica a la empresa (por si el coordinador se borra)
    empresa_id INT,
    FOREIGN KEY (coordinador_id) REFERENCES USUARIO(id) ON DELETE SET NULL,
    FOREIGN KEY (empresa_id) REFERENCES EMPRESA(id) ON DELETE SET NULL
);

-- Tabla ASIGNACION_TAREA (Relación M:N entre Tarea y Técnico)
CREATE TABLE IF NOT EXISTS ASIGNACION_TAREA (
    tarea_id INT,
    tecnico_id INT,
    es_lider BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (tarea_id, tecnico_id),
    FOREIGN KEY (tarea_id) REFERENCES TAREA(id) ON DELETE CASCADE,
    FOREIGN KEY (tecnico_id) REFERENCES USUARIO(id) ON DELETE CASCADE
);

-- Tabla EVIDENCIA
CREATE TABLE IF NOT EXISTS EVIDENCIA (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarea_id INT NOT NULL,
    tecnico_id INT NULL,
    ruta_archivo VARCHAR(255),
    tipo_archivo VARCHAR(50),
    comentario TEXT,
    fecha_subida DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tarea_id) REFERENCES TAREA(id) ON DELETE CASCADE,
    FOREIGN KEY (tecnico_id) REFERENCES USUARIO(id) ON DELETE SET NULL
);

-- Tabla SOLICITUD_INSUMO
CREATE TABLE IF NOT EXISTS SOLICITUD_INSUMO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarea_id INT NOT NULL,
    tecnico_id INT NULL,
    nombre_material VARCHAR(100) NOT NULL,
    cantidad INT DEFAULT 1,
    justificacion TEXT,
    estado ENUM('pendiente', 'aprobada', 'rechazada') DEFAULT 'pendiente',
    fecha_solicitud DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tarea_id) REFERENCES TAREA(id) ON DELETE CASCADE,
    FOREIGN KEY (tecnico_id) REFERENCES USUARIO(id) ON DELETE SET NULL
);

-- Tabla REGISTRO_ACTIVIDAD
CREATE TABLE IF NOT EXISTS REGISTRO_ACTIVIDAD (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarea_id INT,
    usuario_id INT NULL,
    accion VARCHAR(100),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tarea_id) REFERENCES TAREA(id) ON DELETE SET NULL,
    FOREIGN KEY (usuario_id) REFERENCES USUARIO(id) ON DELETE SET NULL
);