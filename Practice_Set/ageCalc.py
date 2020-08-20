from datetime import date


if __name__ == "__main__":

    print('Select from the following options: \n')
    print("1. For Checking by current age ")
    print("2. For Checking by date of birth(in dd:mm:yyyy format) ")

    op = int(input())

    if op == 1:
        age = int(input("Enter your current age: "))

        current_year = date.today().year

        year = int(input("Now enter the year for which you want to determine your age: "))

        if year < (current_year - age):
            print('Sorry You were not born that year')

        elif year > (current_year - age) and year <= 100:
            abs_year = current_year - age
            print(f'Your age in {year} will be {year - abs_year}')

        else:
            abs_year = current_year - age
            print(f'Your age in {year} will be {year - abs_year} maybe you might not be alive that long hope you will!!')

    else:
        dob = input("Enter your date of birth in dd:mm:yyyy format: ")

        year = int(input("Now enter the year for which you want to determine your age: "))

        dob_list = []

        for i in dob.split(':'):
            dob_list.append(i)

        dob_year = int(dob_list[::-1][0])

        current_year = date.today().year

        real_age = year - dob_year

        if real_age < 0:
            print('You were not born that year!!')

        elif real_age < 100:
            print(f'Your age in {year} will be {real_age}')

        else:
            print(f'Your age in {year} will be {real_age} maybe you might not be alive that long hope you will!!')
