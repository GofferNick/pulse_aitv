import psycopg2
# Количество абонентов по типу
def aitv():
    import psycopg2
#Connect to an existing database
conn = psycopg2.connect("host=10.10.100.241 dbname= billing user=reader password = superpuper")


# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("select count(*) from clients;")
all_abon = cur.fetchone()[0]

cur.execute("select count(*) from clients where active = '1' and end_date > CURRENT_DATE  and tarif_plan_id in ('184','185','186','187','188','189','190','191','117', '120','168','169','170','171', '193', '194');")
online_abon = cur.fetchone()[0]

cur.execute("select count(*) from clients where active = '0' and status = 'installed';")
offline_abon=cur.fetchone()[0]

cur.execute("select COUNT(*) from clients where active = '1' and balance < '25' and tarif_plan_id in('184','185','186','187','188','189','190','191' , '117', '120','168','169', '170','171' , '193', '194') and (date_part('days', (current_timestamp - first_activation_date)) > 30  or first_activation_date is NULL) and (date_part('days', (current_timestamp - end_date)) > 60 or end_date is NULL) ;")
deactiv_abon = cur.fetchone()[0]

cur.execute("select count(*) from operations_log, clients where ((EXTRACT(month FROM operations_log.change_time) = '11') and (EXTRACT(year FROM operations_log.change_time) = '2020')) and  clients.tarif_plan_id in('184', '185', '186', '187', '188', '189', '190', '191') and clients.active = '1' and operations_log.new_value = '1' and operations_log.column_name = 'active' and clients.id = operations_log.row_id and ((date_part('days', (current_timestamp - first_activation_date)) > 60) or clients.first_activation_date is null);")
came_back = cur.fetchone()[0]

cur.execute("select count(*) from operations_log, clients where ((EXTRACT(month FROM operations_log.change_time) = '11') and (EXTRACT(year FROM operations_log.change_time) = '2020')) and clients.id = operations_log.row_id  and clients.active = '0' and operations_log.new_value = '0' and operations_log.column_name = 'active';")
deactiv_full = cur.fetchone()[0]
cur.execute("select count(*) from clients where (EXTRACT(month FROM first_activation_date) = '11') and (EXTRACT(year FROM first_activation_date) = '2020');")
install = cur.fetchone()[0]

print("Абоненты aitv: \n")
print("Всего абонентов: " + str(all_abon))
print("Смотрят: " + str(online_abon))
print("На деактивацию: " + str(deactiv_abon))
print("Деактивировано: " + str(offline_abon))
print("Вернувшихся в этом месяце: " + str(came_back))
print("Декактивировано в этом месяце: " + str(deactiv_full))
print("Установок в этом месяце: " + str(install))

# Close communication with the database
cur.close()
conn.close()