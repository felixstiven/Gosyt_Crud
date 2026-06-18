import mysql.connector
import os
import time

# --- VARIABLES DE CONFIGURACIÓN ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1234" 
DB_NAME = "gosyt_db"

SCRIPTS_DIR = "sql_scripts"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    clear_console()
    print("=" * 50)
    print(text.center(50))
    print("=" * 50)


def execute_sql_file(cursor, filename, description):
    print(f"\n[INFO] Procesando: {description}...")
    try:
        # Leer el archivo DE SQL
        with open(os.path.join(SCRIPTS_DIR, filename), 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # Dividir por sentencias, POR CADA (;)
        statements = sql_script.split(';')
        
        for statement in statements:
            statement = statement.strip()
            if statement:
                cursor.execute(statement)
                
        print(f"[OK] {description} completado exitosamente.")
        return True
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo {filename}")
        return False
    except mysql.connector.Error as err:
        print(f"[ERROR SQL] {err}")
        return False
    

def creacion_Base_de_Datos():
    try:
        # Conexión inicial sin base de datos seleccionada
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()
        # Ejecutar script 01
        execute_sql_file(cursor, "01_create_database.sql", "Creación de Base de Datos")
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"[ERROR CONEXIÓN] {err}")


def creacion_Tabla_Bases_de_datos():
    try:
        # Conexión a la base de datos gosyt_db
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = conn.cursor()
        
        execute_sql_file(cursor, "02_create_tables.sql", "Creación de Tablas")
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"[ERROR] Asegúrate de que la base de datos existe. Detalle: {err}")

def Cargar_Datos_dePrueba():
    try:
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        cursor = conn.cursor()
        
        execute_sql_file(cursor, "03_insert_data.sql", "Carga de Datos")
        
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"[ERROR] {err}")

def main():
    creacion_Base_de_Datos
    creacion_Tabla_Bases_de_datos
    Cargar_Datos_dePrueba
