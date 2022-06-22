from command_sender import *

print('Добавление новых строк в таблице')
district = input('Введите номер района: (317) ')
district = 'fl_' + district
fls = input('Введите номер ФЛС: ')

command_add = 'SELECT * FROM {0} WHERE fls = {1};'.format(district, fls)
# Потом добавить возможность выборочно добавлять информацию

sendData(command_add)




