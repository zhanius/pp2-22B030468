import re, csv

phone = input()

def check(s):
    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s))

with open("PhoneBook.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if check(row[3]):
            print(row)