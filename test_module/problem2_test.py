import unittest
import bcrypt
from problem2 import *
from problem1 import *

class problem2_test(unittest.TestCase):

    def setUp(self):
        """
        Setup the Password Manager
        """
        self.pw = PasswordManager(filepath="passwd_test.txt")
        # Creates new empty file for every test case
        with open(self.pw.filepath, "w") as file:
            file.write("")

    def tearDown(self):
        with open(self.pw.filepath, "w") as file:
            file.write("")
        file.close()

    def test_hash_function(self):
        """
        Unit tests to test hash_function()
        """
        password = "Test@123"
        password_false = "Test@12"
        hashed_pw = self.pw.hash_function(password)
        #Testing same passwords
        self.assertTrue(bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8')))

        #Testing different passwords
        self.assertFalse(bcrypt.checkpw(password_false.encode('utf-8'), hashed_pw.encode('utf-8')))

    def test_add_user(self):
        """
        Unit and Integration tests to add users to the Test Password File
        """
        username = "jason"
        username_false = "Fake"
        password = "Test@123"
        role = RolesEnum.CLIENT

        self.pw.add_user(username, password, role)
        with open(self.pw.filepath, "r") as file:
            lines = file.readlines()
            user_info = lines[0].strip().split(",")
            # Testing user is added
            self.assertEqual(username, user_info[0])
            
            #Testing incorrect user added
            self.assertNotEqual(username_false, user_info[0])
        file.close()
    
    def test_user_valid(self):
        """
        Unit and Integration tests for the user_valid() function
        """
        username = "jason"
        username_fake = "Faker"
        password = "Test@123"
        role = RolesEnum.PREMIUM_CLIENT
        # Add user jason to the test password list
        self.pw.add_user(username, password, role)
        
        # Testing username in password file is valid
        self.assertTrue(self.pw.user_valid(username))

        # Testing fake username is not in password file
        self.assertFalse(self.pw.user_valid(username_fake))

    def test_retrieve_user(self):
        """
        Unit and Integration tests for the retrieve_user() function
        """
        username = "jason1"
        username_fake = "Faker1"
        password = "Test@1234"
        password_fake = "Test@Fail1234"
        role = RolesEnum.PREMIUM_CLIENT

        # Add user jason to the test password list
        self.pw.add_user(username, password, role)

        # Testing username in password file is valid
        self.assertDictEqual({"username": username, "role": role.value}, self.pw.retrieve_user(username, password))

        # Testing fake username is not in password file
        self.assertFalse(self.pw.retrieve_user(username_fake, password))

         # Testing wrong password for registered user is not in password file
        self.assertFalse(self.pw.retrieve_user(username, password_fake))

if __name__ == '__main__':
    unittest.main()
