import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
 username = "root", password = "123", database = "mailinfo")

mycursor = mydb.cursor()

def emailEx():
    mycursor.execute("SELECT `email` FROM Details WHERE ID = 1")

    email = str(mycursor.fetchall())

    stremail = ""

    stremail = ''.join(str(e) for e in email)

    return stremail

def passEx():
    mycursor.execute("SELECT `pass` FROM Details WHERE ID = 1")

    password = str(mycursor.fetchall())

    strpass = ''.join(str(i) for i in password)

    return strpass

if __name__ == "__main__":
    emailAddress = emailEx()
    password = passEx()
    pass