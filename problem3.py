from problem1 import *
from problem2 import *
import re

class EnrolUser:
    """
    EnrollUser implements a Registration functionality with a UI, allowing new users to create an account with a secure password and adding their role to allow access to certain permissions.
    """

    def __init__(self, weak_pw_filepath: str = "invalid_passwd.txt"):
        self.ac = AccessControlMechanism()
        self.pw_manager = PasswordManager()
        self.weak_pw_filepath = weak_pw_filepath

    def valid_role(self, role: str) -> str:
        """
        Returns a string representation of the selected role based on the number they selected, or returns None to indicate an invalid role
        """
        match role:
            case "1":
                return RolesEnum.CLIENT
            case "2":
                return RolesEnum.PREMIUM_CLIENT
            case "3": 
                return RolesEnum.FINANCIAL_ADVISOR
            case "4":
                return RolesEnum.FINANCIAL_PLANNER
            case "5":
                return RolesEnum.TELLER
            case _:
                return None                
            
    def check_password(self, username: str, password: str) -> bool:
        """
        Returns True if the password is considered a strong password, meaning that it is not the same as the username, has lengths beetween 8 to 12,
        and includes atleast 1 number, 1 uppercase letter, 1 lowercase letter, and 1 special character. The password can not match any password that is in the weak password file.
        Returns False if any of these conditions are not included.
        """
        if username == password:
            print("Password matches username.")
            return False
        
        if len(password) > 12 or len(password) < 8:
            print("Password must be between 8 and 12 characters in length.")
            return False

        if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%*&]).*$", password):
            print("""
Password must include at least
- one upper-case letter
- one lower-case letter
- one numerical digit
- one special character(!@#$%*&)
""")
            return False
        with open(self.weak_pw_filepath, "r") as file:
            if password in file:
                print("Password is weak.")
                return False
                
        return True

    def register(self):
        """
        Implements a UI to allow users to input their registration information, and continues to run until the registration is successful
        """
        registered = False
        while not registered:
            print("""
-------------------- Register -----------------------------
-----------------------------------------------------------
Roles:
1. Client
2. Premium Client
3. Financial Advisor
4. Financial Planner
5. Teller
""")
            
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (number): ")

            if self.pw_manager.user_valid(username):
                print("Username already exists. Please try again.")
                continue

            elif not self.check_password(username, password):
                print("Invalid password")
                continue

            role_valid = self.valid_role(role)
            while not role_valid:
                print("Role is not valid. Please choose number from above.")
                role = input("Enter role (number): ")
                role_valid = self.valid_role(role)

            self.pw_manager.add_user(username, password, role_valid)
            print("\nSuccessful Registration.")
            registered = True