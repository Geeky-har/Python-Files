def isPal(a):
    return str(a) == str(a)[::-1]

if __name__ == "__main__":

    size = int(input("Enter the size of the initial list: "))
    lst = []

    print(f"Enter {size} elements in the list:")
    for i in range(size):
        item = int(input())
        lst.append(item)

    print("The next Palindromes of the elements in the list are:  ")

    finalList = []

    for e in lst:
        if e <= 10:
            continue
        else:
            if isPal(e):
                finalList.append(e)

            else:
                temp = e + 1
                while not isPal(temp):
                    temp += 1
                
                finalList.append(temp)

    print(finalList)