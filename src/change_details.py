import csv
#make a funtion for change detail
def change(account):
#    open the csv file and write it as file 
    with open("docs//accounts.csv", "r+") as accounts_csv:
        DictReader = csv.DictReader(accounts_csv, delimiter=',')
#    make user select the line they want to delete
#        delete the name and password of the csv file
#    make user input their new name and password 
#    call user registration funtion