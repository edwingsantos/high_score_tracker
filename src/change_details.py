import csv

def change(account):
    new_details = []

    new = input("Would you like a new username? (y/n) ")
    if new == "y":
        new_username = input("What will your new username be? ")
        new_details.append(new_username)
    else:
        new_details.append(account[0])
    new = input("Would you like a new password? (y/n) ")
    if new == "y":
        new_password = input("What will your new password be? ")
        new_details.append(new_password)
    else:
        new_details.append(account[1])
    
    fb_score = input("Would you like to reset your Flappy Bird score? (y/n) ")
    rt_score = input("Would you like to reset your Reaction Time Game score? (y/n) ")
    po_score = input("Would you like to reset your Pong score? (y/n) ")
    
    with open("docs/accounts.csv", "r+") as file:
        reader = csv.DictReader(file)
        rows = list(csv.DictReader(open("docs/accounts.csv")))
        for row in reader:
            if row[0] == account[0]:
                if fb_score == "y":
                    new_details.append("0")
                else:
                    new_details.append(row[2])
                if rt_score == "y":
                    new_details.append("0")
                else:
                    new_details.append(row[3])
                if po_score == "y":
                    new_details.append("0")
                else:
                    new_details.append(row[4])
                rows.pop(row)
        rows.append(new_details)