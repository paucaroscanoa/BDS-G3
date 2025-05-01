from mysql.connector import (connection)

connection = connection.MySQLConnection(
        user='root', 
        password='Mario4190&$',
        host='127.0.0.1',
        database='mpbase')

print('Estas conectado a la base de datos:', connection.database)

# alumno_cursor=connection.cursor()
# alumno_cursor.execute("insert into alumno (nro_documento,nombre) values ('5000','pedro')")
# connection.commit()
# print("alumno insertado")

alumno_cursor_select=connection.cursor()
alumno_cursor_select.execute("select*from alumno")
resultado=alumno_cursor_select.fetchall()
for registro in resultado:
    print('*'*50)
    print(f'NOMBRE: {registro[2]}')

connection.close()