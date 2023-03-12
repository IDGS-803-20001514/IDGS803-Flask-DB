from db import get_connection

# try:
    
#     connection = get_connection()

#     with connection.cursor() as cursor:
#         cursor.execute('call consultar_alumnos()')
#         resultset = cursor.fetchall()

#         for row in resultset:
#             print(row)

#     connection.close()

# except Exception as e:
#     pass

# try:
    
#     connection = get_connection()

#     with connection.cursor() as cursor:
#         cursor.execute('call obtener_alumno(%s)',(4,))
#         resultset = cursor.fetchall()

#         for row in resultset:
#             print(row)
            
#     connection.close()

# except Exception as e:
#     pass

try:
    
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute('call registrar_alumno(%s, %s, %s)',('Cristian Hassel', 'Almaguer Valdez', 'cristian@gmail.com'))
        resultset = cursor.fetchall()

    connection.commit()        
    connection.close()

except Exception as e:
    print(e)