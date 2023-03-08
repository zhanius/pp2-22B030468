import os
#1. Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = input()
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files :")
print([ name for name in os.listdir(path)])

#2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path.
p=os.listdir(r"C:\Users\shakh\Desktop\PP2 Python")

print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))

#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
p = (r"C:\Users\shakh\Desktop\PP2 Python")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")

#4. Write a Python program to count the number of lines in a text file.
f = open(r"C:\Users\shakh\Desktop\PP2 Python\TSIS6\sometext.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))

#5. Write a Python program to write a list to a file.
f = open("smth.txt", "a")
a = ["i", "wrote", "smth"]
for i in a:
    f.write(i)

#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    f = open("{}.txt".format(i), "x")
    
#7. Write a Python program to copy the contents of a file to another file.
f1=open("fromhere.txt", "r")
f2=open("tohere.txt", "w")
for line in f1:
    f2.write(line)

#8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
p=(r"C:\Users\shakh\Desktop\PP2 Python\TSIS6\smthng.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")










