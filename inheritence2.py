# ----------------------Multiple Inheritence--------------------------


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


class Player:
    max_no_of_game = 4

    def __init__(self, name, marks, thappad, kisses, games):
        self.name = name
        self.marks = marks
        self.thappad = thappad
        self.kisses = kisses
        self.games = games

    def show_pdet(self):
        return f"The name of the player is {self.name}, and he plays {self.games}"


class Stud(Player, Student):        # first it will inherit data from Player class then from Student
    no_of_gf = 8

    def printd(self):
        return f'This stud have {self.no_of_gf} keep it up dude'


obj1 = Student('harsh', 89, 20, 3)
obj2 = Player('aditya', 76, 5, 1, ['football', 'cricket'])
obj3 = Stud('Bittu', 56, 12, 200, ['football', 'cricket', 'table tennis'])      # obj of inheriting class

print(obj3.show_pdet())     # base class function used
print(obj3.no_of_gf)        # DERIVED instance variable accessed
print(obj3.no_of_keys)      # parent class of base class variable accessed
