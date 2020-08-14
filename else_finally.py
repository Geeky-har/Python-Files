f = open('test.txt')

try:
    f1 = open('does.txt')

except Exception as e:
    print("The file does.txt is not found in the file system")

else:
    print("This block will run only if exception does not occurs")

finally:
    print("This will run anyway whether exception occurs or not")
    f.close()
    # f1.close()


print("This is very important statement!! Rememeber")
