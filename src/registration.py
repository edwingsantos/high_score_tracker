import csv

while True:
    temp_user = input("Please create a username:\n")
    with open("docs/accounts.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            item = {"username": row.get("username", "").strip(), "password": row.get("password", "").strip(), "flappybird": row.get("flappybird", "").strip(), "reaction time": row.get("reaction time", "").strip(), "pong": row.get("pong.strip")}
            if temp_user == "username":
                print("That username is not availible, would you like to log into that account?")
                
            