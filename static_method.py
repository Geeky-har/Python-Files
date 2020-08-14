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

    @staticmethod
    def greet(string):            # just a simple method in the class
        print(f"hello and welcome {string} to the object oriented programming concepts")


harsh = Employee.from_slash("98/12/50")     # passing arg to the above classmethod defined
aditya = Employee("77", "40", "15")
print(harsh.kisses)
print(aditya.marks)
harsh.greet("harsh")
