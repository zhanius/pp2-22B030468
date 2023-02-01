thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#all key 
for x in thisdict:
  print(x)

#all values
for x in thisdict:
  print(thisdict[x])

#values()
for x in thisdict.values():
  print(x)

#keys()
for x in thisdict.keys():
  print(x)

#items()
for x, y in thisdict.items():
  print(x, y)
  




