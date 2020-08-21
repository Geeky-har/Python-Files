def calc(a, min, max):

    if min == max:
        
        if a/min:
            print(f'Yes the apples can be evenly divided amongst the childrens')

        else:
            print(f'No the apples cannot be evenly divided')

    else:
        for i in range(min, max+1):
            if a % i == 0:
                print(f'Yes {a} apples can be divided evenly with {i} childrens')

            else:
                print(f'No {a} apples cannot be divided evenly with {i} childrens')

if __name__ == "__main__":

    apple = int(input("Enter the number of apples you have!"))
    min = int(input("Now Enter the min number of childrens"))
    max = int(input("Now Enter the max number of childrens"))

    calc(apple, min, max)
