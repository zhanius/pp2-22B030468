import time
import math
#1. Write a Python program with builtin function to multiply all the numbers in a list
a = [1, 2, 3, 4, 5]
print(math.prod(a))

#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s="ThisIsMyString"
cnt1 = 0
cnt2 = 0
for i in s:
    if (i.isupper()):
        cnt1 += 1
    elif (i.islower()):
        cnt2 += 1
print( "Uppercase:", cnt1)
print( "Lowercase:", cnt2)

#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
s1 = (''.join(reversed(s)))
if s == s1:
    print( "Yes, Is a palindrome." )
else:
    print( "No." )

#4. Write a Python program that invoke square root function after specific milliseconds.
n = int(input())
tm = float(input())
time.sleep(tm/1000)
print("The square root of {} after {} miliseconds is:".format(tm,math.sqrt(n)))

#5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
a=[True, False, True]
b=[True, 56, True]


print(all(a))
print(all(b))
