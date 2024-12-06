from problem1 import *
from problem3 import *
from problem4 import *

def perform_option(enrol_users: EnrolUser, login_users: LoginUser, choice: str):
    """
    Returns the option selected by the user, either Login, Register, or Quit. A will run the Login UI, whereas the B will run the Enrol UI, whereas C will exit the system.
    All other options are invalid.
    """
    match choice:
        case "A":
            login = login_users.login()
            if not login:
                print("Returning to Homepage")
                return None
            else:
                return login
        case "B":
            return enrol_users.register()
        case "C":
            print("Exiting System... Have a good day!")
            return quit()
        case _:
            print("Option is not valid. Please try again.")
            
def main():
    """
    The UI for the justInvest prototype. First runs the homepage of the justInvest system, and allows users to input the listed commands to navigate through the app.
    """
    registration = EnrolUser()
    login = LoginUser()
    logged_in = False

    while True:
        print("""
-------------------- justInvest System --------------------
-----------------------------------------------------------
Operations available on the system:
1. View account balance
2. View investment portfolio
3. Modify investment portfolio
4. View Financial Advisor contact info
5. View Financial Planner contact info
6. View money market instruments
7. View private consumer instruments
X. Logout
""")
        if not logged_in:
            print(
"""
-----------------------------------------------------------
Options:
A. Login
B. Register
C. Exit
""")
            user_choice = input("Select option (A B C): ").strip()
            role = perform_option(registration, login, user_choice)
            if user_choice == "A" and role:
                logged_in = True


if __name__ == "__main__":
    main()