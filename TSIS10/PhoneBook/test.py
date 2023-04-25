import psycopg2 
from config import database
config = psycopg2.connect(**database) 
 
current = config.cursor() 
 
create_table = ''' 
INSERT INTO retaked_students VALUES(%s,%s,%s,%s) 
 
''' 
select = ''' 
SELECT * FROM retaked_students; 
''' 
update = ''' 
UPDATE retaked_students SET id = %s  WHERE name = %s; 
''' 
delete= ''' 
DELETE FROM retaked_students WHERE name = %s; 
''' 
#current.execute(create_table, (input(),input(),input(),input())) 
#current.execute(select) 
#db_version = current.fetchall() 
 
#print("Psql version:") 
#print(db_version) 
#current.execute(delete, [input()]) 
current.execute(update, (input(), input())) 
current.execute(select) 
db_version = current.fetchone() 
 
#print("Psql version:") 
print(db_version) 
 
current.close() 
config.commit() 
config.close()