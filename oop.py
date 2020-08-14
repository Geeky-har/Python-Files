class Student:
    no_of_keys = 3      # class variable, will shared by all the objects, objects cannot change this
    pass


harsh = Student()       # object created
aditya = Student()      # object created

harsh.marks = 89
harsh.thappad = 2
harsh.kisses = 99

aditya.marks = 70
aditya.thappad = 10
aditya.kisses = 6

print(aditya.no_of_keys)
Student.marks = 4       # New class variable created
print(Student.marks)
print(Student.__dict__)
aditya.no_of_keys = 10  # new instance variable created
print(aditya.no_of_keys)
print(aditya.__dict__)