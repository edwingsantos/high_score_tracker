import csv
import registration

#make a funtion for change detail
def change(account):
#    open the csv file and write it as file 
    with open("docs//accounts.csv", "r+") as accounts_csv:
        DictReader = csv.DictReader(accounts_csv, delimiter=',')
        with open("docs//accounts.csv", newline="") as f:
            reader = csv.DictReader(f) 
            #read each row as a dictionary
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row['username']}")
#       make user select the line they want to delete
        choice = int(input("Select what file you want to delte from the list above: \n"))
        if 1 <= choice <= i:
            accounts_csv.close()
            #delete the name and password of the csv file
            rows = list(csv.DictReader(open("docs//accounts.csv")))
            rows.pop(choice-1)
            with open("docs//accounts.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        else:
            print("line doesn't exist")
            return
#    call user registration funtion
    registration()
















#    make user input their new name and password 
    new_username = input("Enter new username: \n")
    new_password = input("Enter new password: \n")
    new_account = {"username": new_username, "password": new_password}
    # Append the new account to CSV
    rows.append(new_account)
    with open("docs//accounts.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=new_account.keys())
        writer.writeheader()
        writer.writerows(rows)