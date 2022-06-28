from command_sender import *
from time_tracker import *

print('Добавление новых строк в таблице')
district = input('Введите номер района: (317) ')
district = 'fl_' + district
fls = input('Введите номер ФЛС: ')
name = "'" + input('Введите ФИО должника: ') + "'"
address = "'" + input('Введите адрес: ') + "'"
tel = "'" + input('Введите номер телефона должника: ') + "'"

command_add = 'INSERT INTO {0} (fls, name, address, tel) VALUES ({1}, {2}, {3}, {4});'.format(district, fls, name, address, tel)
# Потом добавить возможность выборочно добавлять информацию

sendData(command_add)

time_now(district, fls)


