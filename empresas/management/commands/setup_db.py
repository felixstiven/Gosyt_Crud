from django.core.management.base import BaseCommand
from pathlib import Path
import mysql.connector
import getpass


class Command(BaseCommand):
    help = 'Configura la base de datos inicial: solicita credenciales, crea la BD, ejecuta los scripts SQL y genera el archivo .env'

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.MIGRATE_HEADING('=== Configuración inicial de la base de datos ==='))

        host: str = input('Host de MySQL (Enter para "localhost"): ') or 'localhost'
        user: str = input('Usuario de MySQL (Enter para "root"): ') or 'root'
        password: str = getpass.getpass('Contraseña de MySQL: ')
        db_name: str = input('Nombre de la base de datos (Enter para "gosyt_db"): ') or 'gosyt_db'

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
        except mysql.connector.Error as error:
            self.stderr.write(self.style.ERROR(f'No se pudo conectar a MySQL: {error}'))
            return

        cursor = connection.cursor()
        self.stdout.write(self.style.SUCCESS('Conexión a MySQL exitosa.'))

        base_dir: Path = Path(__file__).resolve().parent.parent.parent.parent
        sql_scripts_dir: Path = base_dir / 'datos/sql_scripts'

        scripts = [
            '01_create_database.sql',
            '02_create_tables.sql',
            '03_insert_data.sql',
        ]

        for script_name in scripts:
            script_path: Path = sql_scripts_dir / script_name

            if not script_path.exists():
                self.stderr.write(self.style.ERROR(f'No se encontró el archivo: {script_path}'))
                continue

            self.stdout.write(f'Ejecutando {script_name}...')
            sql_content: str = script_path.read_text(encoding='utf-8')

            try:
                for statement in sql_content.split(';'):
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)
                connection.commit()
                self.stdout.write(self.style.SUCCESS(f'{script_name} ejecutado correctamente.'))
            except mysql.connector.Error as error:
                self.stderr.write(self.style.WARNING(f'Aviso en {script_name}: {error}'))

        cursor.close()
        connection.close()

        env_path: Path = base_dir / '.env'
        env_content: str = (
            f'DB_HOST={host}\n'
            f'DB_USER={user}\n'
            f'DB_PASSWORD={password}\n'
            f'DB_NAME={db_name}\n'
        )
        env_path.write_text(env_content, encoding='utf-8')

        self.stdout.write(self.style.SUCCESS(f'Archivo .env creado en: {env_path}'))
        self.stdout.write(self.style.MIGRATE_HEADING('=== Configuración completada ==='))
        self.stdout.write('Ya puedes ejecutar: python manage.py runserver')
        