import unittest
from unittest.mock import patch
from problem4 import *

class problem4_test(unittest.TestCase):

    def setUp(self):
        """
        Setup the Enrol User Class
        """
        self.login = LoginUser()
        self.login.pw_manager = PasswordManager(filepath="passwd_test.txt")
        # Creates new empty file for every test case
        with open(self.login.pw_manager.filepath, "w") as file:
            file.write("")

    def tearDown(self):
        with open(self.login.pw_manager.filepath, "w") as file:
            file.write("")
        file.close()


    @patch("builtins.input", side_effect=["jason", "Test@1234", "1", "X"])
    def test_valid_login(self, side_effect):
        """
        Integration test using the login() UI to test user inputs and ensure that login is successful
        """
        self.login.pw_manager.add_user("jason", "Test@1234", RolesEnum.CLIENT)
        role = self.login.login()

        # Logout works successfully, and logout works successfully
        self.assertEqual(role, None) 

if __name__ == '__main__':
    unittest.main()