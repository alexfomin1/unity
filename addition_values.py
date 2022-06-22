import psycopg2
from config import host_name, user, password, db_name, port_id

print('Добавление новых строк в таблице')
district = input('Введите номер района: (317) ')
district = 'fl_' + district
fls = input('Введите номер ФЛС: ')
name = "'" + input('Введите ФИО должника: ') + "'"
address = "'" + input('Введите адрес: ') + "'"
tel = "'" + input('Введите номер телефона должника: ') + "'"

command_add = 'INSERT INTO {0} (fls, name, address, tel) VALUES ({1}, {2}, {3}, {4});'.format(district, fls, name, address, tel)
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




