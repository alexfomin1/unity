import psycopg2
from config import host_name, user, password, db_name, port_id

print('Добавление новых строк в таблице')
district = input('Введите номер района: (317) ')
district = 'fl_' + district
fls = input('Введите номер ФЛС: ')

command_add = 'SELECT * FROM {0} WHERE fls = {1};'.format(district, fls)
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
        print(cursor.fetchall())    
    
    connection.close()
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)

finally:
    if connection:
        # cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')  




