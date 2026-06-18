import mysql.connector
from decouple import config

#DB_HOST = "localhost"
#DB_USER = "root"
#DB_PASSWORD = "1234"
#DB_NAME = "gosyt_db"

def verificar_conexion():
    try:
        conn = mysql.connector.connect(
            host=config("DB_HOST"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            database=config("DB_NAME")
        )
    
        conn.close()
    
        return {
            "success": True,
            "message": "Conexión a la base de datos exitosa."
        }

    except mysql.connector.Error as err:

        if err.errno == 1045:
            return {
                "success": False,
                "message": "Usuario o contraseña incorrectos."
            }

        elif err.errno == 1049:
            return {
                "success": False,
                "message": "La base de datos no existe."
            }

        elif err.errno == 2003:
            return {
                "success": False,
                "message": "No se pudo conectar al servidor MySQL. Verifique el host o que el servicio esté iniciado."
            }

        return {
            "success": False,
            "message": f"Error de conexión: {err}"
        }


def verificar():
    try:
        # Conectar a la base de datos
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        
        print("=" * 60)
        print("VERIFICACIÓN DE BASE DE DATOS GOSYT")
        print("=" * 60)
        
        # 1. Verificar tablas creadas
        print("\n TABLAS CREADAS:")
        
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        for tabla in tablas:
            print(f"   ✓ {tabla[0]}")
        
        # 2. Verificar cantidad de registros por tabla
        print("\n REGISTROS EN CADA TABLA:")
        cursor.execute("SELECT COUNT(*) FROM EMPRESA")
        print(f"   • EMPRESA: {cursor.fetchone()[0]} registros")
        
        cursor.execute("SELECT COUNT(*) FROM USUARIO")
        print(f"   • USUARIO: {cursor.fetchone()[0]} registros")
        
        cursor.execute("SELECT COUNT(*) FROM TAREA")
        print(f"   • TAREA: {cursor.fetchone()[0]} registros")
        
        cursor.execute("SELECT COUNT(*) FROM ASIGNACION_TAREA")
        print(f"   • ASIGNACION_TAREA: {cursor.fetchone()[0]} registros")
        
        # 3. Mostrar datos
        print("\n EMPRESAS REGISTRADAS:")
        cursor.execute("SELECT id, nombre_empresa, estado FROM EMPRESA")
        empresas = cursor.fetchall()
        for emp in empresas:
            print(f"   ID: {emp[0]} | Nombre: {emp[1]} | Estado: {emp[2]}")
        
        print("\n USUARIOS REGISTRADOS:")
        cursor.execute("SELECT id, nombre, rol, correo FROM USUARIO")
        usuarios = cursor.fetchall()
        for usu in usuarios:
            print(f"   ID: {usu[0]} | Nombre: {usu[1]} | Rol: {usu[2]} | Correo: {usu[3]}")
        
        print("\n TAREAS CREADAS:")
        cursor.execute("SELECT id, titulo, estado, prioridad FROM TAREA")
        tareas = cursor.fetchall()
        for tar in tareas:
            print(f"   ID: {tar[0]} | Título: {tar[1]} | Estado: {tar[2]} | Prioridad: {tar[3]}")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 60)
        print("VERIFICACIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 60)
        
    except mysql.connector.Error as err:
        print(f"\n ERROR: {err}")
        print("\nPosibles causas:")
        print("1. MySQL no está instalado o no está corriendo")
        print("2. La base de datos 'gosyt_db' no existe")
        print("3. La contraseña es incorrecta")

if __name__ == "__main__":
    verificar()
    input("\nPresiona Enter para salir...")



    