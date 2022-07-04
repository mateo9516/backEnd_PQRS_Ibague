import psycopg2
from psycopg2 import DatabaseError
from decouple import config

"""
def config(archivo = 'Base_de_datos.ini', seccion = 'postgresql'):
    parser = ConfigParser()
    parser.read(archivo)


    db = {}
    if parser.has_section(seccion):
        params = parser.items(seccion)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception ('seccion '+seccion+' no encontrada en el archivo '+archivo)
    
    return db
"""

def conectar():
    try:
        return psycopg2.connect(
            host = config("PGSQL_HOST"),
            database = config("PGSQL_DATABASE"),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD')
        )
    except DatabaseError as ex:
        raise ex