from command_sender import *


command_add = '''
ALTER TABLE fl_317_c
ADD COLUMN last_edit VARCHAR(255);
'''

sendData(command_add)