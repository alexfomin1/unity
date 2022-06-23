from command_sender import *
from time_tracker import *

#def import_col(district1, fls1, address1, name1, period1, summa1, summa_sud1, date_sud1, number_sud1, summa_ssp1, remains_ssp1, date_ssp1):

   # command_add = ('
  #  INSERT INTO {0} (fls, address, name, period, summa, summa_sud, date_sud, number_sud, summa_ssp, remains_ssp, date_ssp)
 #   VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11});
#    ').format(district1, fls1, address1, name1, period1, summa1, summa_sud1, date_sud1, number_sud1, summa_ssp1, remains_ssp1, date_ssp1)
  #  time_now(district1, fls1)

def import_col(district1, fls1, address1, name1, period1, summa1, summa_sud1):
    command_add = ('''
    INSERT INTO {0} (fls, address, name, period, summa, summa_sud)
    VALUES ({1}, {2}, {3}, {4}, {5}, {6});
    ''').format(district1, fls1, address1, name1, period1, summa1, summa_sud1)
    sendData(command_add)
    time_now(district1, fls1)    