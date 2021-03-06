# class Employee:
#     no_of_days = 30     # a class variable
#
#     @classmethod
#     def change_var(cls, var):   # takes class and updated value as an arg
#         cls.no_of_days = var
#
#
# harsh = Employee()
# harsh.change_var(31)            # object or class both can change the class variable
#
# print(harsh.no_of_days)
# print(Employee.no_of_days)

# ------------------------------------class method as alternative constructor--------------------------


class Employee:
    no_of_days = 30     # a class variable

    def __init__(self, m, t, k):
        self.marks = m
        self.thappad = t
        self.kisses = k

    @classmethod
    def from_slash(cls, s):            # class method used as a constructor
        # params = s.split("/")           # splitig the string and converting it to a list
        # return cls(params[0], params[1], params[2])         # passing it to the class constructor
        return cls(*s.split("/"))           # oneliner taking the list as an *args


harsh = Employee.from_slash("98/12/50")     # passing arg to the above classmethod defined
aditya = Employee("77", "40", "15")
print(harsh.kisses)
print(aditya.marks)
