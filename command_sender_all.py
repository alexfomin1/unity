import psycopg2
from config import host_name, user, password, db_name, port_id


def sendDataAll(command_addition):
    try:
        connection = psycopg2.connect(
            host=host_name,
            user=user,
            password=password,
            database=db_name,
            port=port_id
        )
            
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(
                command_addition
            )
            return cursor.fetchall()    
        
        connection.close()
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')