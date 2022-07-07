from command_sender_all import *
from tabulate import tabulate

print('Вывод реестра района')
#district = input('Введите номер района: (317) ')
#district = 'fl_' + district
district = 'fl_317'

#command_add = 'SELECT * FROM {0}, {1}, {2}, {3}, {4}, {5}, {6} WHERE fls=fls;'.format(district+'_c', district+'_sud', district+'_ssp', district+'_bank', district+'_restruct', district+'_impossible', district+'_no')



command_add = '''
	SELECT {0}.fls,
        {0}.name,
        {0}.address,
        {0}.tel,
        {0}.summa,
        {0}.period,
        {0}.typeProperty,
        {0}.area,
            
        {1}.summa_sud,
        {1}.date_sud,
        {1}.name_sud,
        {1}.number_sud,
        {1}.scan_sud,
            
        {2}.summa_ssp,
        {2}.remains_ssp,
        {2}.date_ssp,
        {2}.name_ssp,
        {2}.number_ssp,
        {2}.scan_ssp,
            
        {3}.summa_bank,
        {3}.remains_bank,
        {3}.date_bank,
        {3}.name_bank,
        {3}.otozvano_bank,
        {3}.fact_bank,
        {3}.scan_bank,
            
        {4}.summa_restruct,
        {4}.remains_restruct,
        {4}.datesign_restruct,
        {4}.datefinal_restruct ,
        {4}.notification_restruct,
        {4}.scan_restruct,
            
        {5}.summa_impossible,
        {5}.document_impossible,
        {5}.scan_impossible,
            
        {6}.period_less5,
        {6}.summa_less5,
        {6}.period_more5,
        {6}.summa_more5 
	FROM {0}
	FULL JOIN {1}
	ON {0}.fls = {1}.fls

	FULL JOIN {2}
	ON {0}.fls = {2}.fls

	FULL JOIN {3}
	ON {0}.fls = {3}.fls

	FULL JOIN {4}
	ON {0}.fls = {4}.fls

	FULL JOIN {5}
	ON {0}.fls = {5}.fls

	FULL JOIN {6}
	ON {0}.fls = {6}.fls;
	'''.format(district+'_c', district+'_sud', district+'_ssp', district+'_bank', district+'_restruct', district+'_impossible', district+'_no')

s = []
for x in sendDataAll(command_add):
	sp = []
	for y in x:
		if y == 'None':
			sp.append('0')
		else:
			sp.append(str(y))
	s.append(sp)

print(tabulate(s, headers=['ФЛС', 'ФИО', 'Адрес', 'Тел.', 'Сумма долга', 'Период задолженности', 'Тип имущества', 'Площадь', 'Сумма в суде', 'Дата иска', 'Наименование суда', 'Номер иска', 'Скан', 'Сумма в ССП', 'Остаток в ССП', 'Дата подачи в ССП', 'Наименование ССП', 'Номер дела', 'Скан', 'Сумма долга в банке', 'Остаток в банке', 'Дата обращения в банк', 'Наименование банка', 'Отозвано из банка', 'Фактическая сумма', 'Скан', 'Сумма на реструктуризации', 'Остаток', 'Дата подписания', 'Дата окончания', 'Оповещение', 'Скан', 'Сумма невозможного к взысканию', 'Документ-свидетельство', 'Скан', 'Период меньше 5 мес. неотработанный', 'Сумма меньше 5 мес. неотработанная', 'Период больше 5 мес. неотработанный', 'Сумма больше 5 мес. неотработанная'], tablefmt="grid", maxcolwidths=[None, 10]))

