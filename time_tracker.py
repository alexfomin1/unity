from command_sender import *
import datetime


def time_now(dist, fls1):
    now = "'"+str(datetime.datetime.now())+"'"
    command_add = '''
    UPDATE {0}
    SET {1}
    WHERE {2}
    '''.format(dist, 'last_edit=' + now,'fls=' + fls1)
    sendData(command_add)