# NS 1st
import login_logout
import change_details
import registration
from games import flappybird
from games import pong
from games import reactiontime

#Make a function called main
def main():
    found = False
    #make a while loop
    while True:
    #Ask user if they are loged in or if they want to exit
        choice = input("What would you like to do:\n 1: Log in\n 2: Create an account\n 3: Exit\nChoice: ").strip()
        #if user choice is logeg in, call the loged in funtion
        if choice == "1":
            account, found, admin = login_logout.login()
            if found == "register":
                registration.registration()
        #elif user chioce is not loged in, call the not logged in funtion
        elif choice == "2":
            registration.registration()
        elif choice == "3":
            print("Bye bye!")
            return
        else:
            print("Invalid option, try again")
        
        # for once the user is logged in
        if found == True:
            while True:
                choice = input("What would you like to do:\n 1. Flappy Bird\n 2. Reaction Time\n 3. Pong\n 4. Delete Account and Exit\n 5. Log out\nChoice: ").strip()
                if choice == "1":
                    flappybird.flappy_bird(account)
                elif choice == "3":
                    pong.pong(account)
                elif choice == "2":
                    reactiontime.reaction_time_game(account)
                elif choice == "4":
                    change_details.change()
                elif choice == "5":
                    main()
                else:
                    print("Invalid option, try again")
main()