def meth1(lst):
    print("Reverse by inbuilt method: ")
    lst.reverse()
    print(lst)


def swap(a, b):
    x = a
    a = b
    b = x


def meth2(lst):
    print("Reverse by slicing the list: ")
    lst[::-1]
    print(lst)


def meth3(lst):
    i1 = 0
    j = len(lst) - 1

    while i1 < j:
        swap(lst[i], lst[j])
        j -= 1
        i1 += 1

    print("Reverse by custom method (swapping of indexes): ")
    print(lst)


if __name__ == "__main__":

    calorie = []

    n = int(input('Enter the number of items in the list: '))
    
    print('Enter the calories in ascending order of their numbers: ')

    for i in range(n):
        item = int(input())
        calorie.append(item)

    meth1(calorie)

    meth2(calorie)

    meth3(calorie)
