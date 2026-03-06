import csv
import hashlib

def hash_pw(item: str) -> str:
    sha256 = hashlib.sha256()
    sha256.update(item.encode("utf-8"))
    return sha256.hexdigest()

#make a function for login/logout function 
def login():
    found = False

    while True:
        admin = False
        #Ask user to type a username and a password
        username = input("Write your username: ")
        password = input("Write your password: ")
        #if user nanm is admin and password is yippe skipy
        if username == "admin" and password == "YIPPEESKIPPEE":
            found, admin = True, True
            return ["admin", hash_pw("YIPPEESKIPPEE")], found, admin
        #search for the username and the password in the accounts csv
        with open("docs//accounts.csv", mode = "r") as accounts_csv:
            reader = csv.reader(accounts_csv, delimiter=',')
        #if the password and username are in the csv
            for row in reader:
                if username in row and hash_pw(f"{password}") in row:
                    print("\nAccount found!\n")
                    found = True
                    admin = False
                    #break the loop and return logged in with that account
                    #call main function
                    password = hash_pw(f"{password}")
                    return [username, password], found, admin
        #if the password and username are not in the csv
        #print the password and username are invalid
            if not found:
                print(f"{username} not found in csv file")
                register = input("Would you like to register an account (y/n)?")
                if register == "y":
                    register = "register"
                    return None, register, admin
                else:
                    break