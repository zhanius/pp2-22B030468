import psycopg2, csv, re
from config import data
config = psycopg2.connect(**data)
current = config.cursor()

search = """
CREATE OR REPLACE FUNCTION getT (name VARCHAR)
    RETURNS TABLE (
        id INT,
        person_name VARCHAR,
        person_surname VARCHAR,
        phone_number VARCHAR
)
AS $$
BEGIN
    RETURN QUERY SELECT * FROM book WHERE book.person_name ILIKE name OR book.person_surname ILIKE name OR book.phone_number ILIKE name;
END; $$

LANGUAGE PLPGSQL;

SELECT * FROM getT (%s);
"""

update = """
CREATE OR REPLACE PROCEDURE insertT(id INT, name VARCHAR, surname VARCHAR, phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT * FROM Book WHERE person_name = name) THEN
        UPDATE Book SET phone_number = phone WHERE person_name = name;
    ELSE
        INSERT INTO book VALUES(id, name, surname, phone);
    END IF;
END; $$
LANGUAGE PLPGSQL;

CALL insertT(%s, %s, %s, %s);
"""

def check(s):
    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s))

delete = """
CREATE OR REPLACE PROCEDURE deleteT(name VARCHAR)
AS $$
BEGIN
    DELETE FROM Book WHERE book.person_name = name OR book.phone_number = name;
END; $$
LANGUAGE PLPGSQL;

CALL deleteT(%s);
"""

pagination = """
CREATE OR REPLACE FUNCTION getT (lim INT, off INT)
    RETURNS TABLE (
        id INT,
        person_name VARCHAR,
        person_surname VARCHAR,
        phone_number VARCHAR
)
AS $$
BEGIN
    RETURN QUERY SELECT * FROM book ORDER BY book.id LIMIT lim OFFSET off;
END; $$

LANGUAGE PLPGSQL;

SELECT * FROM getT (%s, %s);

"""
     
while True:
    command = input("search, iou, insert, pagination, delete, exit\n")
    
    if command == 'search':
        n = input("Введите имя или фамилию или номер\n")
        word = '%' + n + '%'
        current.execute(search, [word])
        print(*current.fetchall(), sep = '\n')
            
    if command == 'iou':
        id = int(input("Введите ID: "))
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        phone_number = input("Введите номер: ")
        current.execute(update, (id, name, surname, phone_number))

    if command == 'insert':
        with open("PhoneBook.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if check(row[3]):
                    current.execute(update, row)
                else:
                    print(*row)
            config.commit()
    if command == 'delete':

        name = input("Введите имя или номер что удалить: ")
        current.execute(delete, [name])
        config.commit()
    if command == 'exit':
        break
    if command == 'pagination':
        a, b = map(int, input("LIMIT, OFFSET: ").split())
        current.execute(pagination, (a, b))
        print(*current.fetchall(), sep = '\n')
        
current.close()
config.commit()
config.close()