# -------------abstract base class------------------------

from abc import ABC, abstractmethod


class A(ABC):       # This is abstract base class
    @abstractmethod
    def imp_fun(self):      # this is abstract method
        return 0


class B(A):     # this class is inheriting A so it should override abs_method
    def __init__(self, num, cum):
        self.num = num
        self.cum = cum

    def imp_fun(self):
        return f"{self.num + self.cum}"


class C:
    def __init__(self, num, cum):
        self.num = num
        self.cum = cum

    def imp_fun(self):
        return f"{self.num + self.cum}"


if __name__ == '__main__':
    obj1 = B(2, 4)
    obj2 = C(10, 33)
    print(obj1.imp_fun())
    print(obj2.imp_fun())
