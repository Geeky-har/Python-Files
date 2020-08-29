import re

list1 = ['this is good', 'Python is very good', 'Harsh is Python and python is good', 'Python is snake, Python is lang, Python is life']

query = input("Enter the string you want to search: ")

list2 = []

for i in list1:
    if query.lower() in i.lower():
        list2.append(i)

print("The results are: \n")
for e in list2:
    print(e)
