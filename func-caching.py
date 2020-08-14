import time
from functools import lru_cache


@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(3)
    return f"The work has been done and the value is {n}"


if __name__ == '__main__':
    print("Now calling the function")
    print(f"The function returns", some_work(2))
    print(f"Now again calling the function")
    print(f"The function returns", some_work(5))
    print(f"Now again calling the function")
    print(f"The function returns", some_work(2))
