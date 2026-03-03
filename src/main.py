# NS 1st
import login_logout
import change_details
import registration
from games import flappybird
from games import pong
from games import reactiontime

#Make a function called main
def main():
    #make a while loop
    while True:
    #Ask user if they are loged in or if they want to exit
        choice = input("What would you like to do:\n 1: Log in\n 2: Create an account\n 3: Exit\nChoice: ").strip()
        #if user choice is logeg in, call the loged in funtion
        if choice == "1":
            found, admin = login_logout.login()
        #elif user chioce is not loged in, call the not logged in funtion
        elif choice == "2":
            print("Bye bye!")
            return
        else:
            print("Invalid option, try again")
        
        # for once the user is logged in
        if found:
            while True:
                choice = input("What would you like to do:\n 1. Flappy Bird\n 2. Reaction Time\n 3. Pong\n 4. Change account Details\n 5. Log out\nChoice: ").strip()
                if choice == "1":
                    flappybird.flappy_bird()
                elif choice == "2":
                    pong.pong()
                elif choice == "3":
                    reactiontime.reaction_time_game()
                elif choice == "4":
                    change_details.change()
                elif choice == "5":
                    main()
                else:
                    print("Invalid option, try again")
main()