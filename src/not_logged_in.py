#ES 

import main
import login_logout
import registration

while True:
    choice = input("Would you like to:\n1:Log in\n2:Create an account\n3:Log out").strip
    
    if choice == "1":
        login_logout()
    elif choice == "2":
        registration()
    elif choice == "3":
        main()