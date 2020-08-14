def isprime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False

    return True


def primegen(n):
    num = 2
    while n != 0:
        if isprime(num):
            yield num
            n -= 1
        num += 1
    return


if __name__ == '__main__':
    term = int(input('Please Enter the number of prime numbers you want to see'))
    it = primegen(term)
    for _ in it:
        print(_, end=' ')

# this is how we can use generators to find n number of prime numbers where n will be provided by the user
