import re
#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
'''txt = input()
x = re.search(r'ab*?', txt)
print(x)'''

#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
'''txt1 = input()
x1 = re.search( r'ab{2,3}?', txt1)
print(x1)'''

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
'''txt2 = input()
x2 = re.search( r'^[a-z]+\_', txt2)
print(x2)'''

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
'''txt3 = input()
x3 = re.search( r'[A-Z]{1}[a-z]+',txt3)
print(x3)'''

#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
'''txt4 = input()
x4 = re.search( r'^a.*b$', txt4)
print(x4)'''

#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
'''txt5 = input()
x5 = re.sub( '[.,]', ':', txt5)
print(x5)'''

#7. Write a python program to convert snake case string to camel case string.
s = input()
result = re.findall(r'(.*?)_([a-zA-Z])',s)
print(result)
#8. Write a Python program to split a string at uppercase letters.
list = []
s = input()
camel = re.split('_', s)
for i in camel:
    list.append(i.capitalize())
    camel_case = "".join(list)
print(camel_case)


#9. Write a Python program to insert spaces between words starting with capital letters.
s = input()
words = re.findall('.[^A-Z]*', s)
result = ' '.join(words)
print(result)


#10. Write a Python program to convert a given camel case string to snake case.
s = str(input())
result = re.findall('[A-Z][a-z]*', s)
for i in result:
     x = i.lower()
     print(x, end = "_")