import mysql.connector
from mysql.connector import Error


def insertar_alumno(matricula, nombre, apellido, fecha_nac, sexo, direccion, carrera):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = """
                INSERT INTO alumnos (matricula, nombre, apellido, fecha_nacimiento, sexo, direccion, carrera)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (matricula, nombre, apellido, fecha_nac, sexo, direccion, carrera)
            cursor.execute(query, valores)
            conn.commit()
            print("Alumno insertado correctamente.")

    except Error as e:
        print(f"Error al insertar en la base de datos: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def verificar_matricula_existe(matricula):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM alumnos WHERE matricula = %s"
            cursor.execute(query, (matricula,))
            resultado = cursor.fetchone()
            return resultado[0] > 0

    except Error as e:
        print(f"Error al verificar matrícula: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def obtener_alumnos():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = """
                SELECT matricula, nombre, apellido, fecha_nacimiento, sexo, direccion, carrera
                FROM alumnos
                ORDER BY matricula
            """
            cursor.execute(query)
            alumnos = cursor.fetchall()
            return alumnos

    except Error as e:
        print(f"Error al obtener alumnos: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
