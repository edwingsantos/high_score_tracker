import csv
import login_logout.py

#ask user to create a username
username = input("Please input a new username: ")

#open accounts csv and loop through every row
with open("docs/accounts.csv", "r") as file:
    csv_reader = csv.reader()
#    if a row has that username
    for row in csv_reader:
        if username in row:
#        tell the user that there is already and account with that name
            print("There is already an account with that name.")
#        ask them if they would like to try and login to that account
            login = input("Would you like to log in to the user with that name?")
#        if they would
#            call the login_logout function
#        if they want still want to create an account
#            loop back to the beginning of the file (continue in python)
#ask user if they would like a generated password or want to make one themselves
#if they choose to have a password generated for them
#    ask the user to select the requirements they would like for their password
#    generate a password according to those requirements
#    ask the user if they like the password given
#    if they don't
#        loop back through this section (the generate password section)
#if they choose to create a password
#    ask the user for the password they'd like to use
#    ask them to confirm if that's the password they'd like
#    if it isn't
#        loop back through this section (the create password section)
#if their name is admin and their password is YIPPEESKIPPEE
#    make an admin variable true
#otherwise
#    make the admin variable false
#open the accounts csv
#    insert/append a new row on the bottom with the username and password they've inputted and all their scores as 0
#    return back to where it was called with admin