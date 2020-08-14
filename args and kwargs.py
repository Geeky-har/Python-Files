# # def function_name_print(a, b, c, d, e):
# #     print(a, b, c, d, e)
#
#
# def funargs(n, *argsrohan, **kwargsbala):
#     print(n)
#     for item in argsrohan:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes")
#     for key, value in kwargsbala.items():
#         print(f"{key} is a {value}")
#
#
# # function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
#
# har = ["Harry", "Rohan", "Skillf", "Hammad",
#        "Shivam", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
#       "The Programmer": "Coordinator", "Shivam": "Cook"}
# funargs(normal, *har, **kw)


def fun_ar_kwar(p, *args, **fc):        # args accepts lists as an argument, kwargs accepts dict as an argument
    print(p)
    for i in args:
        print(i)
    print('\nNow I will tell you about my fav club in each league:\n')

    for key, value in fc.items():
        print(f"{key}: {value}")


league = ['La liga', 'Bundesliga', 'Premier league', 'Indian Super league']

plain = 'My favourite leagues in the world are'

fav_club = {'La liga': 'Real madrid', 'Bundesliga': 'Dortmund', 'Premier league': 'Chelsea'}

fun_ar_kwar(plain, *league, **fav_club)
