list1 = [True, '23', 10, 20, [1,2,3], 30]
list2 = []

for i in list1:
    if type(i) == int:
        list2.append(i)
    
print("List with hetrogeneous data: ")
print(list1)
print("List with only int data in the above list: ")
print(list2)