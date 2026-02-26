# NS 1st
import login_logout
#Make a function called main
def main():
    #make a while loop
    while True:
    #Ask user if they are loged in or if they want to exit
        choice = input("1:Loged in\n2:Not loged in\n3:Exit\nChoice:").strip()
        #if user choice is logeg in, call the loged in funtion
        if choice == "1":
            print("hi")
        #elif user chioce is not loged in, call the not logged in funtion
        elif choice == "2":
            while True:
                choice = input("Would you like to:\n1:Log in\n2:Create an account\n3:Log out").strip
   
                if choice == "1":
                    login_logout()
                elif choice == "2":
                    registration()
                elif choice == "3":
                    main()

        #elif user choice is exit, break
        elif choice == "3":
            break
        #else print select an actual option
        else:
            print("Invalid option, try again")
main()