class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property           # this wil make it as a property(email can be accesed as a instance)
    def email(self):
        return f"The email of the emp is {self.fname}.{self.lname}@xyz.com"

    @email.setter       # this allows us to set this attribute manually and with that we can set other
    def email(self, strng):     # related attribute to it too
        name = strng.split('@')[0]
        self.fname = name.split('.')[0]
        self.lname = name.split('.')[1]


if __name__ == '__main__':
    obj1 = Employee("harsh", "negi")
    obj2 = Employee("aditya", "singh")

    print(obj1.email)       # using property deco we can accesss and modify it
    obj1.email = "kutta.kamina@xyz.com"
    print(obj1.email)
    print(obj1.fname)
    print(obj1.lname)
