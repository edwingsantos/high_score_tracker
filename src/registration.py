import csv
import login_logout
import random
import string


def registration():
    while True:
        #ask user to create a username
        username = input("Please input a new username: ").strip()

        #open accounts csv and loop through every row
        with open("docs/accounts.csv", newline="") as file:
            csv_reader = list(csv.DictReader(file))
            header = ["username", "password", "score for flappybird", "score for reaction time", "score for pong"]
        #if a row has that username
        for row in csv_reader:
            if username == row["username"]:
    #tell the user that there is already and account with that name
                print("There is already an account with that name.")
    #ask them if they would like to try and login to that account
                login = input("Would you like to log in with that name? (Y/N)").strip().upper()
    #if they would
                if login == "Y":
    #call the login_logout function
                    login_logout.login()
    # if they want still want to create an account
                if login == "N":
    # loop back to the beginning of the file (continue in python)
                    continue
        #ask user if they would like a generated password or want to make one themselves
        password_choice = input("What would you like to do: \n 1. Type your own password \n 2. Generate a new password\nChoice: ").strip()

        if password_choice != "1" and password_choice != "2":
            password_choice = "1"
        #if they choose to have a password generated for them
        if password_choice == "1":
        #    ask the user to select the requirements they would like for their password
            while True:
                password = input("Please enter your new password:\n")
    #            ask them to confirm if that's the password they'd like
                confirm = input("Confirm your password:\n")
                if password == confirm:
                    break
                else:
                    print("Passwords do not match. Try again.")

        # if they don't
        elif password_choice == "2":
        #    generate a password according to those requirements
            #make a funtion called lower
            def lower():
                #return string ascii lower as a list 
                return list(string.ascii_lowercase)
            #make another funtion for upper case
            def upper():
                #return string ascii upper as a list 
                return list(string.ascii_uppercase)
            #make another funtion for numbers
            def nums():
                #return string as number in a list 
                return list(string.digits)
            #make another funtion for special character
            def special_chact():
                #return string for special digits 
                return list(string.punctuation)
            #make a funtion for check 
            def check(choice):
                #make a while loop, make answer equals input what the user says 
                while True:
                    answer = input(choice).strip().upper()
                    #if the answer is yes return true
                    if answer == "Y":
                        return True
                    #if the answer equals no return false
                    elif answer == "N":
                        return False
                    #else print to select an actuel option
                    else:
                        print("please select an actuel option")
            #make a funtion called generate 
            def generate():
                #Make a while loop
                while True:
                    #   make lenght equal an integer input, asking how long the password is going to be
                    length = input("How long does the password need to be: ")
                    #if lenght is digit, break else print to select a number
                    if length.isdigit():
                        length = int(length)  # convert to integer for later use
                        break
                    else:
                        print("Select another option that is a number")
                        continue
                #make the different options to choose equals check with the quiestion 
                lower_case = check("Does the password need lowercase letters (Y/N): ")
                upper_case = check("Does the password need uppercase letters (Y/N): ")
                numbers = check("Does the password need numbers (Y/N): ")
                special_character = check("Does the password need special characters (Y/N): ")
                #make a empty library called requirements
                requirements = []
                #if the quiestion equals yes, add it to requiremnets according to the quiestion
                if lower_case:
                    requirements += lower()
                if upper_case:
                    requirements += upper()
                if numbers:
                    requirements += nums()
                if special_character:
                    requirements += special_chact()
                #if there is nothing is requirements print that you have to put things to create, then return
                if not requirements:
                    print("you must have a requirement")
                    return generate()
                print("\nPassword:")
                #make a loop 4 times, for i in range
                for i in range(1):
                    #make password empty and do another loop, but now in range lenght
                    password = ""
                    for i in range(length):
                        #make password add random choice from requrements. Then print the password
                        password += random.choice(requirements)
                    print(password)
                return password
            password = generate()
        #   save new account to CSV
        new_row = {"username": username, "password": password.strip('"'), 
                   "score for flappybird": "0", "score for reaction time": "0", "score for pong": "0"}
        with open("docs/accounts.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if f.tell() == 0:  
                # if file is empty, write header
                writer.writeheader()
            writer.writerow(new_row)
        print(f"Account for '{username}' created successfully!")
        #   break the loop
        break  