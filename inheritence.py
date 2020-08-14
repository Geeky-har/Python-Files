# ----------------------single inheritence in python--------------------


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


class Player(Student):
    max_no_of_game = 4

    def __init__(self, name, marks, thappad, kisses, games):
        self.name = name
        self.marks = marks
        self.thappad = thappad
        self.kisses = kisses
        self.games = games

    def show_pdet(self):
        return f"The name of the player is {self.name}, and he plays {self.games}"


harsh = Student("harsh", 89, 2, 99)       # object created
aditya = Player("aditya", 60, 10, 3, ['football', 'cricket'])      # object created

print(aditya.no_of_keys)
print(aditya.show_pdet())
print(aditya.__dict__)

