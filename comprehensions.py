# ---------Comprehensions-------------------

# list compreension:

# lst = []
# lst = [i * 3 for i in range(1, 11)]
# print(lst)


# dict comprehension:

# dict1 = {i: f'item{i}' for i in range(100) if i % 10 == 0}
# print(dict1)
#
# dict2 = {value : key for key, value in dict1.items()}       # this will reverse the key value pairs
# print(dict2)
#
# # set comprehensions:
#
# list_food = ["Burger", "Chowmein", "Momos", "Chicken", "Burger", "Momos"]
#
# set1 = {food for food in list_food}
# print(set1)

# generator comprehension:

gen = (i for i in range(1, 100) if i % 2 != 0)
print(gen)

for _ in gen:
    print(_)

