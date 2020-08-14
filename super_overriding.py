# -----------super method and method overrriding----------------


class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"     # instance variable of object
        self.classvar1 = "Instance var in class A"          # instance variable of object
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"       # overrided class variable

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()          # this super() will move control to the overrided constructor of above class
        # print(super().classvar1)


a = A()
b = B()

print(b.classvar1)      # will access instance variable from constructor of class B(with super() at beg)
print(b.special)

