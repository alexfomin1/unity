import psycopg2
from config import host_name, user, password, db_name, port_id


def sendData(dist, a, b):
    try:
        connection = psycopg2.connect(
            host=host_name,
            user=user,
            password=password,
            database=db_name,
            port=port_id
        )
            
        connection.autocommit = True
        
        # change values
        with connection.cursor() as cursor:
            cursor.execute('''
            UPDATE {0}
            SET {1}
            WHERE {2};
            '''.format(dist, a, b)
            )
            print('[INFO] Values are changed successfully')    
        
        connection.close()
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed') 

def decideSearch():
    print('''Как будет осуществляться поиск должника?
    1) по ФЛС
    2) по Фамилии Имени Отчеству
    ''')
    decision = input('Введите цифру (1/2): ')
    return decision


def insertData(district1, s1, fls1='0', name1='0', tel1='0', address1='0'):
    list1 = [tel1, address1]
    sp = ['tel', 'address']
    for i in range(len(sp)):
        if list1[i] != '0':
            if s1 == True:
                sendData(district1, sp[i] + '=' + list1[i],'fls=' + fls1)
            elif s1 == False:
                sendData(district1, sp[i] + '=' + list1[i],'"name" = ' + "'" + name1 + "'")
                #sendData(district1, sp[i] + '=' + list1[i],'name=' + name1)
                

def choiceMaker():
    c = input('Введите нужные цифры/цифру в порядке возрастания через пробел: ')
    return c






print('ИЗМЕНЕНИЕ ДАННЫХ О ДОЛЖНИКЕ')
district = input('Введите номер района: (317) ')
district = 'fl_' + district

# Флажок - поиск по ФЛС/ФИО true-флс
s = True

fl = True
d = decideSearch()
while fl == True:
    if d == '1':
        fl = False
        fls = input('Введите номер ФЛС: ')
        name = '0'
    elif d == '2':
        fl = False
        s = False
        name = input('Введите полностью Фамилию Имя Отчество должника: ')
        fls = '0'
    else:
        print('Неверно введены данные, нужна цифра 1 или 2, попробуйте еще раз')
        d = decideSearch()


print('''
Выберите данные, которые хотите поменять:
1) адрес
2) номер телефона должника
''')


choice = choiceMaker()
fl = True
while fl == True:
    if len(choice) == 1:
        if choice == '1':
            fl = False
            address = "'" + input('Введите адрес: ') + "'"
            insertData(fls1=fls, name1=name, district1=district, address1=address, s1=s)
        elif choice == '2':
            fl = False
            tel = "'" + input('Введите номер телефона должника: ') + "'"
            insertData(fls1=fls, name1=name, district1=district, tel1=tel, s1=s)
        else:
            print('Неверно введены данные, нужна цифра 1 или 2, попробуйте еще раз')
            choice = choiceMaker()            
    elif len(choice) == 3:
        choice = choice.split()
        if choice == ['1', '2']:
            fl = False
            address = "'" + input('Введите адрес: ') + "'"
            tel = "'" + input('Введите номер телефона должника: ') + "'"
            insertData(fls1=fls, name1=name, district1=district, address1=address, tel1=tel, s1=s)
        else:
            print('Неверно введены данные, нужна цифра 1 или 2, попробуйте еще раз')
            choice = choiceMaker()        
    else:
        print('Неверно введены данные, нужна цифра 1 или 2, попробуйте еще раз')
        choice = choiceMaker() 