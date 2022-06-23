from import_of_column import *
import xlrd


def dva(nach):
    nach = float(f'{nach:.2f}')
    return str(nach)

def val_str(x1, y1):
    val_t = sheet.cell(y1, x1)
    a = str(val_t).split(':')
    a = a[1]
    
    if a == "''":
        return ''
    else:
        if "'" in a:
            a = a.split("'")
            a = a[1]
        if '.' in a and ' ' not in a:
            a = a.split('.')
            a = a[0]
        return a

# импорт таблицы
book = xlrd.open_workbook('внуково.xlsx')
sd = {}
for s in book.sheets():
    sd[s.name] = s
sheet = sd['Лист1']

district2 = 'fl_317'
fls2 = ''
address2 = ''
name2 = ''
period2 = ''
summa2 = ''
summa_sud2 = ''
date_sud2 = ''
number_sud2 = ''
summa_ssp2 = ''
remains_ssp2 = ''
date_ssp2 = ''
l_req1 = [fls2, address2, name2, period2, summa2, summa_sud2, date_sud2, number_sud2, summa_ssp2, remains_ssp2, date_ssp2]
l_req = [fls2, address2, name2, period2, summa2, summa_sud2, date_sud2, number_sud2, summa_ssp2, remains_ssp2, date_ssp2]
'''
for j in range(len(l_req)):
    l_req[j] = ''
    l_req[j] = val_str(j, 0+5)

'''

for i in range(164):
    for j in range(len(l_req)):
        l_req[j] = ''
        l_req[j] = val_str(j, i+5)
    import_col(district2, l_req[0], "'"+l_req[1]+"'", "'"+l_req[2]+"'", l_req[3], l_req[4], l_req[5])

# import_col(district2, l_req[0], "'"+l_req[1]+"'", "'"+l_req[2]+"'", l_req[3], l_req[4], l_req[5], l_req[6])

# import_col(district2, fls2, address2, name2, period2, summa2, summa_sud2, date_sud2, number_sud2, summa_ssp2, remains_ssp2, date_ssp2)
