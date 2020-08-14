class Student:
    no_of_keys = 3      # class variable, will shared by all the objects, objects cannot change this

    def __init__(self, n, m, t, k):    # this is a constructor, here self is the object for which it is running
        self.name = n
        self.marks = m          # assigning values the instance variable
        self.thappad = t
        self.kisses = k

    def showdet(self):          # this is a member fuction, here self is the object for which it is running
        return f"name is {self.name} the marks is {self.marks}," \
               f" thappad ki sankhya {self.thappad}, pappi ki sankhya {self.kisses}"

    def printd(self):
        print(f"name is {self.name} the marks is {self.marks}, thappad ki sankhya {self.thappad},"
              f" pappi ki sankhya {self.kisses}")


harsh = Student("harsh", 89, 2, 99)       # object created
aditya = Student("aditya", 70, 10, 6)      # object created

# harsh.marks = 89
# harsh.thappad = 2
# harsh.kisses = 99
#
# aditya.marks = 70
# aditya.thappad = 10
# aditya.kisses = 6

# print(harsh.kisses, aditya.kisses)
harsh.printd()
print(aditya.showdet())
