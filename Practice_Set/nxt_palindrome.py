def is_palindrome(n):
    return str(n) == str(n)[::-1]


def pali(n):

    if is_palindrome(n):
        print(f"{n} is a palindome number")

    else:
        n += 1
        while not is_palindrome(n):
            n += 1

        print(f"{n} is the next palindrome")


if __name__ == '__main__':
    num = int(input("Enter a number to check its next palindrome: "))

    pali(num)
