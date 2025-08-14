import mysql.connector
from mysql.connector import Error


def agregar_campo_foto():
    """Agregar el campo 'foto' a la tabla alumnos para almacenar la ruta de la foto"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Verificar si el campo ya existe
            cursor.execute("""
                SELECT COUNT(*) 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE table_schema = 'registro_alumnos_poo' 
                AND table_name = 'alumnos' 
                AND column_name = 'foto'
            """)

            existe_campo = cursor.fetchone()[0] > 0

            if not existe_campo:
                # Agregar el campo foto
                alter_query = """
                    ALTER TABLE alumnos 
                    ADD COLUMN foto VARCHAR(255) DEFAULT NULL
                """
                cursor.execute(alter_query)
                conn.commit()
                print("Campo 'foto' agregado exitosamente a la tabla alumnos.")
            else:
                print("El campo 'foto' ya existe en la tabla alumnos.")

    except Error as e:
        print(f"Error al modificar la base de datos: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    agregar_campo_foto()
