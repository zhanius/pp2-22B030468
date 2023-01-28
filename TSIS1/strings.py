print("Hello")
print('Hello')

a = "Hello"
print(a)

#Multiline strings:
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)


#Strings are arrays:
t = "Hello, World!"
print(t[1])

#Looping through a string:
for x in "banana":
  print(x)

#Length of a string:
g = "Hello, World!"
print(len(g))


#Check string:
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

#Check if not:
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")




