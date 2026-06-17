# Sistema de Gestión de Tareas Operativas — GoSYT - Crud

Plataforma de gestión de tareas operativas por empresa, desarrollada en Django + MySQL. Versión de prueba sin autenticación real: el contexto de empresa, usuario y rol se gestiona mediante la URL.


## Ejecucion Rapida

```
python -m venv venv
```
```
venv\Scripts\activate
```
```
pip install -r requirements.txt
```
```
python manage.py setup_db
```
```
python manage.py runserver
```


## Requisitos previos

Antes de empezar, asegúrate de tener instalado en tu computador:

- Python 3.12 o superior
- MySQL Server (con MySQL Workbench o cliente de línea de comandos)
- Visual Studio Code (o el editor de tu preferencia)

Puedes verificar tu versión de Python con:

```
python --version
```


## 1. Clonar o descargar el proyecto

Descarga la carpeta completa del proyecto y ábrela en tu editor de código.

## 2. Crear el entorno virtual

Un entorno virtual aísla las librerías de este proyecto del resto de tu computador. Desde la raíz del proyecto (donde está `manage.py`), ejecuta:

```
python -m venv venv
```

Esto crea una carpeta `venv/` con un Python independiente para el proyecto.

## 3. Activar el entorno virtual

**En Windows:**
```
venv\Scripts\activate
```

**En Mac/Linux:**
```
source venv/bin/activate
```

Sabrás que el entorno está activo porque verás `(venv)` al inicio de la línea en tu terminal:

```
(venv) C:\Users\TuUsuario\proyecto_crud>
```

> Recuerda activar el entorno virtual cada vez que abras una nueva terminal para trabajar en el proyecto.

## 4. Instalar las dependencias

Con el entorno virtual activo, instala todas las librerías necesarias de una sola vez:

```
pip install -r requirements.txt
```

Esto instalará Django, el conector de MySQL y las demás dependencias listadas en `requirements.txt`.

## 5. Configurar VS Code para el entorno virtual (opcional pero recomendado)

Si usas VS Code y ves advertencias de importación (por ejemplo "Import could not be resolved"):

1. Presiona `Ctrl + Shift + P`
2. Escribe `Python: Select Interpreter`
3. Selecciona el interprete que esté dentro de la carpeta `venv`

## 6. Configurar la base de datos

El proyecto incluye un comando que automatiza la creación de la base de datos y la generación del archivo de configuración `.env`. Ejecuta:

```
python manage.py setup_db
```

El comando te pedirá:

- Host de MySQL (Enter para usar `localhost`)
- Usuario de MySQL (Enter para usar `root`)
- Contraseña de MySQL
- Nombre de la base de datos (Enter para usar `gosyt_db`)

Con esos datos, el comando:

1. Se conecta a tu servidor MySQL local.
2. Ejecuta en orden los scripts de `sql_scripts/` (`01_create_database.sql`, `02_create_tables.sql`, `03_insert_data.sql`).
3. Genera automáticamente el archivo `.env` en la raíz del proyecto con la configuración de conexión.

> Si la base de datos ya existe en tu MySQL local, el comando puede mostrar avisos de "ya existe" en algunos pasos. Esto es esperado y no representa un error: significa que esa parte ya estaba creada.

## 7. Verificar que todo esté correctamente conectado

```
python manage.py check
```

Si todo está bien, verás:

```
System check identified no issues (0 silenced).
```

## 8. Ejecutar el servidor de desarrollo

```
python manage.py runserver
```

Abre tu navegador en:

```
http://127.0.0.1:8000/empresas/
```

Desde ahí puedes navegar por todo el sistema siguiendo el flujo: Empresas → Usuarios → Tareas → Asignaciones → Evidencias / Insumos / Actividad.

## Estructura del proyecto

```
proyecto_crud/
├── config/             Configuración central del proyecto (settings, urls)
├── empresas/            CRUD de empresas
├── usuarios/             CRUD de usuarios
├── tareas/               CRUD de tareas + pantalla de asignaciones
├── evidencias/           CRUD de evidencias (solo técnico líder)
├── insumos/               CRUD de solicitudes de insumos (solo técnico líder)
├── actividad/             Registro de actividad (cualquier técnico asignado)
├── templates/             Plantillas HTML de todos los módulos
├── datos/                  Scripts auxiliares de consulta (independientes de Django)
├── sql_scripts/            Scripts de creación e inserción de datos en MySQL
├── requirements.txt        Dependencias del proyecto
└── manage.py
```

## Datos de prueba incluidos

El script `03_insert_data.sql` incluye datos de ejemplo listos para usar:

- 3 empresas
- 10 usuarios por empresa (1 administrador, 2 coordinadores, 7 técnicos)
- 10 tareas distribuidas entre las empresas
- Asignaciones de técnicos con un líder definido por tarea
- Evidencias, solicitudes de insumos y registros de actividad asociados

Todos los usuarios de prueba usan la contraseña `1234`.
