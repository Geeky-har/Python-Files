# -------------------------dunder methods and operator overloading------------------------


# class Employee:
#     def __init__(self, name, salary, designation):
#         self.name = name
#         self.salary = salary
#         self.designation = designation
#
#     def __repr__(self):     # this executes when the whole obj is printed
#         return f"(repr)The name of the employee is {self.name}, salary is {self.salary} and he is a {self.designation}"
#
#     def __str__(self):      # does the same but get more preference
#         return f"(str)The name of the employee is {self.name}, salary is {self.salary} and he is a {self.designation}"
#
#
# if __name__ == '__main__':
#     emp1 = Employee("Harsh", 400, "Dev")
#     emp2 = Employee("Aditya", 200, "Manager")
#
#     print(emp2)     # this will print str
#     print(repr(emp1))       # this will print repr


class Complex:      # created a class for performing operations on complex no.
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def print_num(self):
        return f'The result is {self.num1} and {self.num2}'

    def __add__(self, other):       # + operator overloaded
        result = Complex(self.num1 + other.num1, self.num2 + other.num2)
        return result

    def __sub__(self, other):       # - operator overloaded
        result1 = Complex(self.num1 - other.num1, self.num2 - other.num2)
        return result1

    def __mul__(self, other):       # * operator overloaded
        result2 = Complex(self.num1 * other.num1, self.num2 * other.num2)
        return result2

    def __truediv__(self, other):      # / operator overloaded
        result3 = Complex(self.num1 / other.num1, self.num2 / other.num2)
        return result3


if __name__ == '__main__':
    obj1 = Complex(2, 3)
    obj2 = Complex(6, 2)
    sum1 = obj1 + obj2
    sub1 = obj1 - obj2
    mul1 = obj1 * obj2
    div1 = obj1 / obj2

    print(sum1.print_num())
    print(sub1.print_num())
    print(mul1.print_num())
    print(div1.print_num())
