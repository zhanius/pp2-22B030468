#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() 1:
for x in range(6):
  print(x)

#2:
for x in range(2, 6):
  print(x)

#3:
for x in range(2, 30, 3):
  print(x)

#else: 1.
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

#2:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.

#nested loops:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


