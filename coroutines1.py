import time


def find(n):
    f = open("cour1.txt", "r")
    file = f.read()
    time.sleep(2)  # lets assume it takes 2 seconds to read the above file from the system

    while True:
        n = (yield)     # will use find() as a couroutine

        if n in file:
            print(f"Yes {n} you are my friend!! Congratulations")

        else:
            print(f"Sorry {n} we aren't friends yet!!")


if __name__ == '__main__':

    lst = []

    i = int(input("Please enter the number of friends you want to enter: "))

    print(f"Now enter {i} names of student: ")

    for _ in range(i):          # will input the list of names
        name = input()
        lst.append(name)

    print("Please wait for a second.....")

    c = find(lst[0])      # instantiate the coroutine
    next(c)             # will start the coroutine

    for horah in lst:
        c.send(horah)        # will send the name to the coroutine

    c.close()                # will close the coroutine
