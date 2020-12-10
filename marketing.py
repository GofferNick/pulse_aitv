import psycopg2
# Количество абонентов по типу
def aitv():
    import psycopg2
#Connect to an existing database
conn = psycopg2.connect("host=10.10.100.241 dbname= billing user=reader password = superpuper")


# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("select count(*) from clients where tarif_plan_id = '193';")
standprem = cur.fetchone()[0]

cur.execute("select count(*) from clients where tarif_plan_id = '194';")
prostoy = cur.fetchone()[0]

cur.execute("select count(*) from operations_log, clients where ((EXTRACT(month FROM operations_log.change_time) = '11') and (EXTRACT(year FROM operations_log.change_time) = '2020')) and clients.id = operations_log.row_id  and operations_log.new_value = '193' and operations_log.column_name = 'tarif_plan_id';;")
online_abon = cur.fetchone()[0]

cur.execute("select count(*) from operations_log, clients where ((EXTRACT(month FROM operations_log.change_time) = '11') and (EXTRACT(year FROM operations_log.change_time) = '2020')) and clients.id = operations_log.row_id  and operations_log.new_value = '194' and operations_log.column_name = 'tarif_plan_id';;")
new_abon_prostoy = cur.fetchone()[0]

cur.execute("select card_id from clients where active = 1 and tarif_plan_id = ' 193' and (date_part('days', (current_timestamp - end_date)) > 3)")
offline_abon= cur.fetchall()

cur.execute("select COUNT(*) from clients where active = '1' and balance < '25' and tarif_plan_id in('184','185','186','187','188','189','190','191' , '117', '120','168','169', '170','171') and (date_part('days', (current_timestamp - first_activation_date)) > 30  or first_activation_date is NULL) and (date_part('days', (current_timestamp - end_date)) > 60 or end_date is NULL) ;")
deactiv_abon = cur.fetchone()[0]

cur.execute("select card_id from operations_log, clients where   clients.id = operations_log.row_id  and operations_log.new_value = '193' and operations_log.column_name = 'tarif_plan_id' and clients.active = '1' and (date_part('days', (current_timestamp - operations_log.change_time)) > 365);")
came_back = cur.fetchall()



print("Абоненты aitv: \n")
print("Количество абонентов Стандарт Премиум АКЦИЯ: " + str(standprem))
print("Количество абонентов Тариф Простой: " + str(prostoy))
print("Подключились к Стандарт+Премиум Акция в этом месяце:  " + str(online_abon))
print("Подключились к Простой в этом месяце:  " + str(new_abon_prostoy))
print("Кто не смотрит Стандарт Премиум Акция больше 3 дней:  " + str(offline_abon))
print("Абоненты, которые перешли на Стандарт Премиум Акцию Год назад  " + str(came_back))


# Close communication with the database
cur.close()
conn.close()