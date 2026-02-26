import csv
import main

#make a function for login/logout function 
def login_logout(search):

    found = False
    while True:
        #Ask user to type a username and a password
        username = input("Write your username: ")
        password = input("Write your password: ")
        #search for the username and the password in the accounts csv
        with open("docs//accounts.csv", mode = "r") as accounts_csv:
            reader = csv.reader(accounts_csv, delimiter=',')
        #if the password and username are in the csv
            for row in reader:
                if search in row:
                    print("Found")
                    found = True
                    #break the loop and return logged in with that account
                    #call main function
                    main()
        #if the password and username are not in the csv
        #print the password and username are invalid
            if not found:
                print(f"{search} not found in csv file")
                continue

    
   

    #if user nanm is admin and yippe skipy
        if username == "admin":
            print("hi")
        if username == "yippe skipy":
            print("hi")
        #call admin function

login_logout(search="")

        