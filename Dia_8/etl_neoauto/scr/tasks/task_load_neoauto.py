from mysql.connector import (connection)
from prefect import task

@task(name="Carga de data en base de datos")
def task_load_neoauto(autos):
    try:
        conn = connection.MySQLConnection(
            user='root', 
            password='Mario4190&$',
            host='127.0.0.1',
            database='mpbase'
            )
        cursor = conn.cursor()
        
        query_table = """CREATE TABLE IF NOT EXISTS autos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            url VARCHAR(255),
            precio DOUBLE
        )"""
        cursor.execute(query_table)
        
        query_insert = "INSERT INTO autos (nombre, url, precio) VALUES (%s, %s, %s)"
        
        for auto in autos:
            cursor.execute(query_insert, (auto['nombre'], auto['url'], auto['precio']))
        
        conn.commit()
        cursor.close()
        conn.close()
        print("datos guardados en bd...")
    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))