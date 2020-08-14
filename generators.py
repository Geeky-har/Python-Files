# --------------Generators in python----------------


def gen(n):
    for i in range(1, n):
        yield i             # it will provide value of i


a = gen(2000)           # a function for generatin no upto 2000 created

print(a.__next__())     # will print 1 since it starts from 1
print(a.__next__())     # will print 2 as next function will iterate it to one
print(a.__next__())     # --do--
print(a.__next__())     # --do--
