# In this file we will make a program to find average using variable args


def avg(*t):
    return sum(t)/len(t)


if __name__ == '__main__':
    ans = avg(10, 20, 30)
    print(ans)
