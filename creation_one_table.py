import psycopg2
from config import host_name, user, password, db_name, port_id


try:
#connect to exist database
    connection = psycopg2.connect(
        host=host_name,
        user=user,
        password=password,
        database=db_name,
        port=port_id
    )
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE fl_317_journal (
            fls BIGINT NOT NULL PRIMARY KEY,
            message_journal VARCHAR(255),
            summa_journal INTEGER,
            date_journal DATE,
            date_input_jornal DATE,
            appointment_journal VARCHAR(255)
            );'''
        )
        print('[INFO] Table created successfully')      
    
    connection.close()
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)

finally:
    if connection:
        # cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
        
'''
summa_sud INTEGER,
date_sud DATE,
name_sud VARCHAR(255),
number_sud VARCHAR(255),
scan_sud VARCHAR(255),
            
            summa_ssp INTEGER,
            remains_ssp INTEGER,
            date_ssp DATE,
            name_ssp VARCHAR(255),
            number_ssp VARCHAR(255),
            scan_ssp VARCHAR(255),
            
            summa_bank INTEGER,
            remains_bank INTEGER,
            date_bank DATE,
            name_bank VARCHAR(255),
            otozvano_bank VARCHAR(255),
            fact_bank INTEGER,
            scan_bank VARCHAR(255),
            
            summa_restruct INTEGER,
            remains_restruct INTEGER,
            dateSign_restruct DATE,
            dateFinal_restruct  DATE,
            notification_restruct VARCHAR(255),
            scan_restruct VARCHAR(255),
            
            summa_impossible INTEGER,
            document_impossible VARCHAR(255),
            scan_impossible VARCHAR(255),
            
            period_less5 INTEGER,
            summa_less5 INTEGER,
            period_more5 INTEGER,
            summa_more5 INTEGER
'''