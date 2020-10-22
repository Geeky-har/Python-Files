# Taylors Expansion of sin(x): x - x3/3! + x5/5! - x7/7! + x9/9! - .....

def fact(a):
    ans = 1
    while a > 0:
        ans *= a
        a -= 1

    return ans

def calc_sin(x, i):
    total = x
    power = 3

    if i == 1:
        return total
    
    for i in range(2, i+1):
        if i%2 == 0:
            total -= (x**power) / (fact(power))

        else:
            total += (x**power) / (fact(power))

        power += 2

    return total

def draw_exp(x, i):
    if i == 1:
        print(x)
        return

    power = 3
    print(x, end='')
    for i in range(2, i+1):
        if i % 2 == 0:
            print(f' - {x}^{power}/{power}!', end='')

        else:
            print(f' + {x}^{power}/{power}!', end='')

        power += 2


if __name__ == "__main__":
    x = int(input('Enter the value of x: '))
    i = int(input('Enter the number of iterations in the equation:'))

    ans = calc_sin(x, i)
    draw_exp(x, i)
    print(' = ', end='')
    print(ans)