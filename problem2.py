import bcrypt
from problem1 import RolesEnum

class PasswordManager:
    """
    The PasswordManager deals with the password file, and managing users by adding new entries to the file, hashing passwords using bcrypt,
    checking for duplicate usernames, and verifying valid user login
    """

    def __init__(self, filepath: str = "passwd.txt"):
        self.filepath = filepath

    def hash_function(self, password: str) -> str:
        """
        Returns a string of the hashed and salted password over 12 rounds
        """
        pw_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt(12)
        hashed_pw = bcrypt.hashpw(pw_bytes, salt)
        return hashed_pw.decode('utf-8')

    def add_user(self, username: str, password: str, role: RolesEnum) -> None:
        """
        Adds a record of the user to the password file
        """
        hashed_pw = self.hash_function(password)

        user_entry = f"{username}, {hashed_pw}, {role.value}\n"
        try:
            with open(self.filepath, "a") as file:
                if not self.user_valid(username):
                    file.write(user_entry)
        except FileNotFoundError:
            print("File does not exist")

    def user_valid(self, username: str) -> bool:
        """
        Returns True if the username is already used in the password manager file, False otherwise
        """
        with open(self.filepath, "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if user_info[0] == username:
                    return True
            return False
        
    def retrieve_user(self, username: str, password: str):
        """
        Return a dictionary containing the user's username and role from the password file list, for when the user logs in, otherwise return False and print out the error
        """
        try:
            with open(self.filepath, "r") as file:
                for line in file:
                    user_info = line.strip().split(", ")
                    if user_info[0] == username:
                        if bcrypt.checkpw(password.encode('utf-8'), user_info[1].encode('utf-8')):
                            return {
                                "username": user_info[0],
                                "role": user_info[2]
                            }
                        print("\nPassword does not match")
                        return False
                print("\nUser does not exist")
                return False

        except FileNotFoundError:
            print("File does not exist")