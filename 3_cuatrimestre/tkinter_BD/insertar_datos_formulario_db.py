import mysql.connector
from mysql.connector import Error


def insertar_alumno(
    matricula,
    nombre,
    apellido,
    curp,
    fecha_nac,
    sexo,
    direccion,
    carrera,
    foto_blob=None,
):
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
                INSERT INTO alumnos (matricula, nombre, apellido, curp, fecha_nacimiento, sexo, direccion, carrera, foto)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                matricula,
                nombre,
                apellido,
                curp,
                fecha_nac,
                sexo,
                direccion,
                carrera,
                foto_blob,
            )
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
                SELECT matricula, nombre, apellido, curp, fecha_nacimiento, sexo, direccion, carrera
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


def obtener_alumno_por_matricula(matricula):
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
                SELECT matricula, nombre, apellido, curp, fecha_nacimiento, sexo, direccion, carrera, foto
                FROM alumnos
                WHERE matricula = %s
            """
            cursor.execute(query, (matricula,))
            alumno = cursor.fetchone()
            return alumno

    except Error as e:
        print(f"Error al obtener alumno: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def actualizar_alumno(
    matricula_original,
    matricula,
    nombre,
    apellido,
    curp,
    fecha_nac,
    sexo,
    direccion,
    carrera,
    foto_blob=None,
):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Si hay foto_blob, actualizar también la foto
            if foto_blob is not None:
                query = """
                    UPDATE alumnos 
                    SET matricula = %s, nombre = %s, apellido = %s, curp = %s, fecha_nacimiento = %s, 
                        sexo = %s, direccion = %s, carrera = %s, foto = %s
                    WHERE matricula = %s
                """
                valores = (
                    matricula,
                    nombre,
                    apellido,
                    curp,
                    fecha_nac,
                    sexo,
                    direccion,
                    carrera,
                    foto_blob,
                    matricula_original,
                )
            else:
                query = """
                    UPDATE alumnos 
                    SET matricula = %s, nombre = %s, apellido = %s, curp = %s, fecha_nacimiento = %s, 
                        sexo = %s, direccion = %s, carrera = %s
                    WHERE matricula = %s
                """
                valores = (
                    matricula,
                    nombre,
                    apellido,
                    curp,
                    fecha_nac,
                    sexo,
                    direccion,
                    carrera,
                    matricula_original,
                )

            cursor.execute(query, valores)
            conn.commit()
            print("Alumno actualizado correctamente.")

    except Error as e:
        print(f"Error al actualizar en la base de datos: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def eliminar_alumno(matricula):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = "DELETE FROM alumnos WHERE matricula = %s"
            cursor.execute(query, (matricula,))
            conn.commit()
            print("Alumno eliminado correctamente.")

    except Error as e:
        print(f"Error al eliminar de la base de datos: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def verificar_matricula_existe_excepto(matricula, matricula_original):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
    except Error as e:
        print(f"Error al verificar matrícula: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Funciones para manejar calificaciones
def obtener_calificaciones(matricula):
    """Obtiene todas las calificaciones de un alumno"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT materia, calificacion FROM calificaciones WHERE matricula = %s ORDER BY materia"
            cursor.execute(query, (matricula,))
            calificaciones = cursor.fetchall()
            return calificaciones

    except Error as e:
        print(f"Error al obtener calificaciones: {e}")
        return []

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def insertar_o_actualizar_calificacion(matricula, materia, calificacion):
    """Inserta o actualiza una calificación"""
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
                INSERT INTO calificaciones (matricula, materia, calificacion)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE calificacion = VALUES(calificacion)
            """
            cursor.execute(query, (matricula, materia, calificacion))
            conn.commit()
            return True

    except Error as e:
        print(f"Error al insertar/actualizar calificación: {e}")
        raise e

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def calcular_promedio(matricula):
    """Calcula el promedio de calificaciones de un alumno"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()
            query = "SELECT AVG(calificacion) FROM calificaciones WHERE matricula = %s"
            cursor.execute(query, (matricula,))
            resultado = cursor.fetchone()
            return round(resultado[0], 2) if resultado[0] else 0

    except Error as e:
        print(f"Error al calcular promedio: {e}")
        return 0

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# ==================== FUNCIONES ADICIONALES PARA CALIFICACIONES ====================


def insertar_calificacion(matricula, materia, calificacion):
    """Inserta o actualiza una calificación"""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro_alumnos_poo",
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Usar INSERT ... ON DUPLICATE KEY UPDATE para actualizar si ya existe
            query = """
            INSERT INTO calificaciones (matricula, materia, calificacion)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            calificacion = VALUES(calificacion),
            fecha_registro = CURRENT_TIMESTAMP
            """

            cursor.execute(query, (matricula, materia, calificacion))
            conn.commit()
            return True

    except Error as e:
        print(f"Error al insertar calificación: {e}")
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def obtener_calificaciones_alumno(matricula):
    """Obtiene todas las calificaciones de un alumno"""
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
            SELECT materia, calificacion, fecha_registro 
            FROM calificaciones 
            WHERE matricula = %s
            ORDER BY materia
            """

            cursor.execute(query, (matricula,))
            calificaciones = cursor.fetchall()
            return calificaciones

    except Error as e:
        print(f"Error al obtener calificaciones: {e}")
        return []

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
