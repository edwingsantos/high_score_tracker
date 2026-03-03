import csv
import login_logout
def registration():
    while True:
        #ask user to create a username
        username = input("Please input a new username: ")
    
        #open accounts csv and loop through every row
        with open("docs/accounts.csv", "r") as file:
            csv_reader = csv.reader()
        #    if a row has that username
            for row in csv_reader:
                if username in row:
    #           tell the user that there is already and account with that name
                    print("There is already an account with that name.")
                else:
    #           ask them if they would like to try and login to that account
                    login = input("Would you like to log in with that name? (Y/N)").strip()
    #               if they would
                    if login == "Y":
    #               call the login_logout function
                        login_logout()
    #               if they want still want to create an account
                    if login == "N":
    #               loop back to the beginning of the file (continue in python)
                        continue
        #ask user if they would like a generated password or want to make one themselves
        password_choice = input("What would you like to do: \n 1. Type your own password \n 2. Generate a new password\nChoice: ")
             #if they choose to have a password generated for them
        if password_choice == "1":
        #    ask the user to select the requirements they would like for their password
            requirements = input("What requrements would you like?")
        #    generate a password according to those requirements
        #    ask the user if they like the password given
    
         # if they don't
        elif password_choice == "2":
        
        #        loop back through this section (the generate password section)
        #if they choose to create a password
        #    ask the user for the password they'd like to use
        #    ask them to confirm if that's the password they'd like
        #    if it isn't
        #        loop back through this section (the create password section)
        #if their name is admin and their password is YIPPEESKIPPEE
        if username == "admin" and password == "YIPPEESKIPPEE":
        #    make an admin variable true
            admin = True
        #otherwise
        else:
        #    make the admin variable false
            admin = False
        #open the accounts csv
        with open("docs/accounts.csv", "a") as file:
        #    insert/append a new row on the bottom with the username and password they've inputted and all their scores as 0
        #    return back to where it was called with admin
    