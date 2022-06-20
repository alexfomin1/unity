import psycopg2
from config import host_name, user, password, db_name, port_id

print('Добавление новых строк в таблице')
fls_in = input('Введите номер ФЛС: ')
name_in = "'" + input('Введите ФИО должника: ') + "'"
address_in = "'" + input('Введите адрес: ') + "'"
tel_in = "'" + input('Введите номер телефона должника: ') + "'"

command_add = 'INSERT INTO about (fls, name, address, tel) VALUES ({0}, {1}, {2}, {3});'.format(fls_in, name_in, address_in, tel_in)
# Потом добавить возможность выборочно добавлять информацию

try:
    connection = psycopg2.connect(
        host=host_name,
        user=user,
        password=password,
        database=db_name,
        port=port_id
    )
        
    connection.autocommit = True
    
    # add values
    with connection.cursor() as cursor:
        cursor.execute(
            command_add
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




