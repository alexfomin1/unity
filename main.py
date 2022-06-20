import psycopg2
from config import host_name, user, password, db_name, port_id

try:
#connect to exist database
    connection = psycopg2.connect(
        host=host_name,
        user=user,
        password=password,
        database=db_name,
        port=port_id
    )
        
    connection.autocommit = True
    # cursor = connection.cursor()
    #server version
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Server version: {cursor.fetchone()}')
        
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE about (
            fls int NOT NULL PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255),
            tel VARCHAR(255)
            );'''
        )
        print('[INFO] Table created successfully')    
    
    # add values
    with connection.cursor() as cursor:
        cursor.execute(
            '''INSERT INTO about (fls, name, address, tel) VALUES
            (123456, 'Иван Иванов', 'Коштоянца 12', '9233435435');'''
        )
        print('[INFO] Values are added successfully')    
    
    connection.close()
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)

finally:
    if connection:
        # cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
