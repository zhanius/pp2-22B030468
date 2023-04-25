import psycopg2,csv
from config import data
config = psycopg2.connect(**data)
current = config.cursor()

insert = """
    INSERT INTO PhoneBook VALUES(%s,%s,%s) returning *;
"""

update = """
    UPDATE PhoneBook SET phone_number = %s WHERE person_name = %s;
"""

select = """
    SELECT * FROM PhoneBook;
"""

delete = """
    DELETE FROM PhoneBook WHERE person_name = %s;
"""

while True:
    command = input("insert, update, select, delete, exit\n")
    
    if command == 'insert':
        n = int(input("Если хотите загрузить с csv файла введите 1, иначе 2\n"))
        if n == 1:
            with open("PhoneBook.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    current.execute(insert, row)
            config.commit()
        if n == 2:
            name = input("Введите имя:")
            surname = input("Введите фамилию:")
            phoneNumber = input("Введите номер:")
            current.execute(insert, (name, surname, phoneNumber))
            config.commit()
            
    if command == 'update':
        name = input("Введите имя:")
        phone_number = input("Введите номер:")
        current.execute(update, (phone_number,name))
        config.commit()
    if command == 'select':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        config.commit()
    if command == 'delete':
        name = input("Введите имя:")
        current.execute(delete, [name])
        config.commit()
    if command == 'exit':
        break

current.close()
config.commit()
config.close()