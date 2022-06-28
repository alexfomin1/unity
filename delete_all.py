from command_sender import *

def del_all(dist, type1):
    command_add('''
    DELETE FROM {}
    ''').format('fl_'+dist+'_'+type1)
    sendData(command_add)