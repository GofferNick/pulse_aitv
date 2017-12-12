# Количество абонентов по типу
import psycopg2
#Connect to an existing database
conn = psycopg2.connect("host=10.10.100.241 dbname= billing user=reader password = superpuper")
# Open a cursor to perform database operations
cur = conn.cursor()
f = open('test.csv', 'w')
cur.execute("select hash, card_id, firstname, lastname, middlename, phone,end_date  from clients where active = '1' and balance < '25' and tarif_plan_id in('184','185','186','187','188','189','190','191' , '117', '120','168','169', '170','171') and (date_part('days', (current_timestamp - first_activation_date)) > 30  or first_activation_date is NULL) and (date_part('days', (current_timestamp - end_date)) > 60 or end_date is NULL);")
deactiv_abon = cur.fetchall()
for record in deactiv_abon:
    f.write(str(record) + '\n')
    print (record)


# Close communication with the database
f.close()
cur.close()
conn.close()