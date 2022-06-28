from command_sender import *

print('Удаление должника!')
district = input('Введите номер района: ')
fls = input('Введите номер ФЛС: ')

def del_one(dist, fls1, type1):
    command_add = ('''
    DELETE FROM {0}
    WHERE fls={1};
    ''').format('fl_'+dist+'_'+type1, fls1)
    sendData(command_add)
    
list_s = ['c','sud','ssp','bank','restruct','impos','no']

for x in list_s:
    del_one(district, fls, x)