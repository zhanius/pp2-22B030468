thisset = {"apple", "banana", "cherry"}
print(thisset)


#duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#set items
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#can contain dif-t data types
set1 = {"abc", 34, True, 40, "male"}

#type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#the set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

