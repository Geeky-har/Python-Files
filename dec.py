# this is all about decorators


def deco(func):
    def exe():
        print("Executing")
        func()
        print("Executed")
    return exe


# @deco
# def test():
#     print("this is a test text you can ignore it")


# alternative way to call decorator function
def test():
    print("this is a test file you can ignore it")


test = deco(test)

test()
