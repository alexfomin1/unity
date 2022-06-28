from command_sender import *
from command_sender_one import *
from command_sender_all import *
from districts_list import fl_317
from xlutils.copy import copy
from xlrd import open_workbook

start_y = 4

districts = ['fl_317_']
w1 = open_workbook('СИР ГБУ свыше 5 мес..xlsx', on_demand=True)
w = copy(w1)
for x in districts:
    start_x = 2
    start_y += 1
    command_add = ('''
    SELECT COUNT(fls)
    FROM {}
    ''').format(x+'c')
    a = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa)
    FROM {}
    ''').format(x+'c')
    b = sendDataOne(command_add)[0]
    
    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'sud')
    c = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_sud)
    FROM {}
    ''').format(x+'sud')
    d = sendDataOne(command_add)[0]
    
    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'ssp')
    e = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_ssp)
    FROM {}
    ''').format(x+'ssp')
    f = sendDataOne(command_add)[0]

    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'bank')
    g = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_bank)
    FROM {}
    ''').format(x+'bank')
    h = sendDataOne(command_add)[0]
    
    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'restruct')
    i = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_restruct)
    FROM {}
    ''').format(x+'restruct')
    j = sendDataOne(command_add)[0]
    
    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'impossible')
    k = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_impossible)
    FROM {}
    ''').format(x+'impossible')
    l = sendDataOne(command_add)[0]
    
    command_add = ('''
    SELECT COUNT(DISTINCT fls)
    FROM {}
    ''').format(x+'no')
    m = sendDataOne(command_add)[0]
    command_add = ('''
    SELECT SUM(summa_more5)
    FROM {}
    ''').format(x+'no')
    n = sendDataOne(command_add)[0]
    
    list_par = []
    for y1 in (a,b,c,d,e,f,g,h,i,k,l,m,n):
        if y1 == None:
            y1 = 0
            list_par.append(y1)
        else:
            list_par.append(y1)
    for abc in range(len(list_par)):
        w.get_sheet(0).write(start_y,start_x, int(list_par[abc]))
        start_x += 1
w.save('report.xls') 