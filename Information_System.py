from datetime import datetime

name = input('Please Enter Your Name here!!')

print("Please select from the following options to see something about the specific person: ")

print("1. For Harsh Negi")
print("2. For Dalip Singh Negi")
print("3. For Bittu Singh")

n = input()

if n == '1':
    f = open("harsh.txt")
    c = f.read()
    print(c)

    print("\nWant to add something for him? y/n")
    t = input()

    if t == 'y':
        print("Please write something about him: ")
        i = input()

        samay = datetime.now()
        csamay = samay.strftime('%d/%m/%y, %H:%M:%S')
        fptr = open("harsh.txt", "a")
        con = fptr.write('\n' + i + "  " + "(added at " + csamay + "  " + "by " + name + ")")

        print("\nThanks! Your Information is valuable for us!!")

    f.close()


elif n == '2':
    f = open("dalip.txt")
    c = f.read()
    print(c)

    print("\nWant to add something for him? y/n")
    t = input()

    if t == 'y':
        print("Please write something about him: ")
        i = input()

        samay = datetime.now()
        csamay = samay.strftime('%d/%m/%y, %H:%M:%S')
        fptr = open("dalip.txt", "a")
        con = fptr.write('\n' + i + "  " + "(added at " + csamay + "  " + "by " + name + ')')

        print("\nThanks! Your Information is valuable for us!!")

    f.close()


else:
    f = open("bittu.txt")
    c = f.read()
    print(c)

    print("\nWant to add something for him? y/n")
    t = input()

    if t == 'y':
        print("Please write something about him: ")
        i = input()

        samay = datetime.now()
        csamay = samay.strftime('%d/%m/%y, %H:%M:%S')
        fptr = open("bittu.txt", "a")
        con = fptr.write('\n' + i + "  " + "(added at " + csamay + "  " + "by " + name + ")")

        print("\nThanks! Your Information is valuable for us!!")

    f.close()
