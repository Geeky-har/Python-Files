def find_num(num1, lst1):
    for items in range(len(lst)):
        if lst[items] == num1:
            return True

    return False


print("Enter the number of elements in the list: ")
n = int(input())

lst = []

print("Now enter the items in the list :")

for i in range(n):
    item = input()
    lst.append(item)

num = input("Now enter the number you want to find: ")

flag = find_num(num, lst)

if flag:
    print("Found")

else:
    print("Not Found")

