from problem1 import *
from problem2 import *

class LoginUser:
    """
    LoginUser implements the Login functionality with the UI, allowing already registered users to login with their username and password to gain access to the justInvest app.
    Once logged in, the user gains access to their authorized operations
    """
    def __init__(self):
        self.ac = AccessControlMechanism()
        self.ac.define_role_permissions()
        self.pw_manager = PasswordManager()

    def login(self):
        """
        Implements a UI requesting for the User to login in with their credentials. The User has 3 attempts to login, in which if they are unable to successfully login,
        The login UI will terminate. If the user logs in successfully, they are welcomed into their account in which they gain access to their authorized operations.
        Tellers are required to input their time of login, and are requested/denied permission of their operations based if they log in during the businesses hours of operations
        """
        login_attempts = 0
        while login_attempts < 3:
            login_attempts +=1
            print("""
-------------------- Login --------------------------------
-----------------------------------------------------------
""")
            username = input("Enter username: ")
            password = input("Enter password: ")

            if self.pw_manager.retrieve_user(username, password):
                user_info = self.pw_manager.retrieve_user(username, password)
                print(f"""
-------------------- ACCESS GRANTED ------------------------
-------------------- Welcome {user_info["username"]}! ---------------
Role: {user_info["role"]}
""")
                if user_info["role"] == RolesEnum.TELLER.value:
                    while True:
                        time_hour = input("Enter current hour at login (0 - 23)").strip()
                        if int(time_hour) < 0 or int(time_hour) > 23:
                            print("Invalid hour, please try again.")
                            continue
                        while True:
                            time_minutes = input("Enter current minute at login (0 - 59)").strip()
                            if int(time_minutes) < 0 or int(time_minutes) > 59:
                                print("Invalid minute, please try again.")
                                continue
                            break 
                        break
                    if int(time_hour) >= 9 and int(time_hour) <=16 or (int(time_hour) == 17 and int(time_minutes) == 0):
                        self.ac.set_business_hours(True)
                    else:
                        self.ac.set_business_hours(False)

                logged_in = True
                while logged_in:
                    self.ac.print_operations(user_info["role"])
                    user_choice = input("Which operation would you like to perform?: ")
                    self.ac.perform_operation(user_info["role"], user_choice)
                    if user_choice == "X":
                        print("\nLogging out...")
                        logged_in = False
                        user_info["role"] = None

                return user_info["role"]
            print(f"Unsuccessful login attempt: {login_attempts} of 3")
        return None