# program of geometric series
# 1/2 + 1/4 + 1/8 + 1/16 +... to nth term
import math

def patt(n):
    pattern = ""
    pattern += "1/2"

    for i in range(2, n+1):
        val = int(math.pow(2, i))
        pattern += f" + 1/{val}"

    return pattern

def calc(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/(int(math.pow(2,i)))

    return sum


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    if n == 0:
        raise Exception("value 0 for term not allowed")
    pattern = patt(n)
    val = calc(n)
    print(f"The value of geometric equation {pattern} = {val}")