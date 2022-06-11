def registration():
    db = open("database.txt","r")
    import re
    pattern ="([a-zA-Z]+@+[A-Za-z{1-5}]+.+[a-z{1-3}])"
    username= input("Create Username:")
    result =re.findall(pattern,username)
    if not result:
        print("Invalid username: username should have @ and followed by dot  there should not be any dot immediate next to @")
        db.close()
        registration()
    else:
        pattern1= "^(?=.{5,16})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        password = input("Create Password:")
        result = re.findall(pattern1, password)
        if not result:
            print("Invalid password: password (5 < password length > 16) Must have minimum one special character,one digit,one uppercase, one lowercase character")
            db.close()
            registration()
        else:
            confirmPassword = input("Confirm Password:")
            username_arr = []
            pass_arr = []
            for i in db:
                if i is None:
                    print("asdf")
                else:
                    x, y = i.split(", ")
                    y = y.strip()
                    username_arr.append(x)
                    pass_arr.append(y)
                    data= dict(zip(username_arr, pass_arr))
            if password != confirmPassword:
                print("password don't match, Try again")
                db.close()
                registration()
            elif username in username_arr:
                print("username already exists")
                db.close()
                registration()
            else:
                db = open("database.txt", "a")
                db.write(username + ", " + password + "\n")
                db.close()
                print("success")


def login():
    db = open("database.txt", "r")
    username = input("Enter Username:")
    password = input("Enter Password:")
    if len(password or username)<1:
        print("Invalid username or password")
        db.close()
        login()
    else:
        username_arr = []
        pass_arr= []
        for i in db:
            x, y = i.split(", ")
            y = y.strip()
            username_arr.append(x)
            pass_arr.append(y)
        data = dict(zip(username_arr, pass_arr))
        if username not in username_arr:
            print("username does not exist")
            db.close()
            registration()
        else:
            try:
                if data[username]:
                    if password == data[username]:
                        print("login successful")
                        print("Hi,", username)
                    else:
                        print("incorrect password")
            except:
                print("incorrect username or password")
    db.close()


def forgotPassword():
    db = open("database.txt", "r")
    username = input("Enter Username:")
    flag=False
    oldpassword=""

    for i in db:
        x, y = i.split(", ")
        y = y.strip()
        if x==username:
            oldpassword=y
            flag=True
            break

    if (not flag):
        print("username doesn't exists. Please Go For Registration First")
        db.close()
    else:
        select=input("type, 1 for Original Password | 2 for New Password")
        if select== "1":
            print("Your Original Password is:",oldpassword)
            db.close()
        elif select== "2":
            newpassword = input("Create New Password:")
            confirmNewPassword = input("Confirm New Password:")
            db = open("database.txt", "rt")
            data=db.read()
            data = data.replace(username + ", " + oldpassword, username + ", " + newpassword)
            db.close()
            db = open("database.txt", "wt")
            db.write(data)
            db.close()



def home(option=None):
    option=input("Type, 1 for Login | 2 for Signup | 3 for Forgot Password:")
    if option== "1":
        login()
    elif option== "2":
        registration()
    elif option== "3":
        forgotPassword()
    else:
        print("Invalid input. Please select correct input")
        home()
home()


