import csv
import registration

#make a funtion for change detail
def change():
#    open the csv file and write it as file 
    with open("docs//accounts.csv", "r+") as accounts_csv:
        DictReader = csv.DictReader(accounts_csv, delimiter=',')
        with open("docs//accounts.csv", newline="") as f:
            reader = csv.DictReader(f) 
            #read each row as a dictionary
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row['username']}")
#       make user select the line they want to delete
        choice = int(input("Select what file you want to delete from the list above: \n"))
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