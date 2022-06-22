from command_sender import *

print('Добавление новых строк в таблице')
district = input('Введите номер района: (317) ')
district = 'fl_' + district

command_add = 'DROP TABLE {};'.format(district)


sendData(command_add)




