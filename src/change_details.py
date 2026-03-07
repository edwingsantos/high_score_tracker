import csv
import login_logout

def change(account):
    new_details = []
    print()

    new = input("Would you like a new username? (y/n) ")
    if new == "y":
        new_username = input("What will your new username be? ")
        new_details.append(new_username)
    else:
        new_details.append(account[0])
    new = input("Would you like a new password? (y/n) ")
    if new == "y":
        new_password = input("What will your new password be? ")
        new_details.append(login_logout.hash_pw(new_password))
    else:
        new_details.append(account[1])
    
    fb_score = input("Would you like to reset your Flappy Bird score? (y/n) ")
    rt_score = input("Would you like to reset your Reaction Time Game score? (y/n) ")
    po_score = input("Would you like to reset your Pong score? (y/n) ")
    
    with open("docs/accounts.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
        
    for row in rows:
        if not row:
            continue
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
            rows.remove(row)
            break

    rows.append(new_details)

    with open("docs/accounts.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(row for row in rows if row)
    
    print()