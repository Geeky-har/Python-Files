# this is how we read a text file in py
#
# f = open("test.txt")
# p = f.read()
# print(p)
# f.close
#
# this is how we append a text in an existing file
#
# f = open("test.txt", "a")
# f.write("\nthis text is just appended in this file after its creation!!")
# f.close()
#
# to read the contents of a file line by line:
#
# f = open("test.txt")
# for line in f:
#     print(line, end="")
# f.close
#
# to store each line of the text in a list:
#
# f = open("test.txt")
# lst = f.readlines()
# print(lst)
# f.close
#
# this is how we create a new file using write method
# f = open("zeher.txt", "w")
# a = f.write("Yeh file sirf yeh dekhne ke liye banai gyi hai ki kya yeh kaam krti hai ya nhi")
# print(a)        # it prints the number of characters written in the file
# f.close()
#
# to open a file in r+ mode we can read and append at the same time
#
# f = open("zeher.txt", "r+")
# print(f.read())
# f.write("\nDhanyawad apka jo app yaha padhare ")
# f.close()
#
# tell and seek function
#
# f = open("test.txt", "r")
# print(f.tell())
# print(f.readline())
# print(f.tell())         # this tells us the current position of our file pointer
# print(f.readline())
# f.seek(100)               # this will take the file pointer back to the mentioned character
# print(f.tell())
# print(f.readline())     # will print one line from the file
# f.close()

# handling files with using with block

# with open("zeher.txt") as f:
#     c = f.readline()
#     print(c)
