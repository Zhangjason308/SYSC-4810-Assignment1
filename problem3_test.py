import unittest
from unittest.mock import patch
from problem2 import *
from problem3 import *

class problem3_test(unittest.TestCase):

    def setUp(self):
        """
        Setup the Enrol User Class
        """
        self.eu = EnrolUser()
        self.eu.pw_manager = PasswordManager(filepath="passwd_test.txt")
        # Creates new empty file for every test case
        with open(self.eu.pw_manager.filepath, "w") as file:
            file.write("")

    def tearDown(self):
        with open(self.eu.pw_manager.filepath, "w") as file:
            file.write("")
        file.close()

    def test_valid_role(self):
        """
        Unit tests to test valid_role()
        """
        role = "1"

        # Valid role 
        self.assertEqual(RolesEnum.CLIENT, self.eu.valid_role(role))

        # Valid role is not equal to any other role
        self.assertNotEqual(RolesEnum.PREMIUM_CLIENT, self.eu.valid_role(role))

        # Not valid role
        self.assertIsNone(self.eu.valid_role("6"))

    def test_check_password(self):
        """
        Unit tests to test check_password()
        """
        username = "Jason"
        strong_pw = "Test@1234"
        weak_pw_length = "Test@12"
        weak_pw_user = "Jason"
        weak_pw_condition = "11111111"
        weak_pw_weak_lst = "123456789"

        # Strong password
        self.assertTrue(self.eu.check_password(username, strong_pw)) 

        # Weak password equal to username
        self.assertFalse(self.eu.check_password(username, weak_pw_user))

        # Weak password doesn't meet required length
        self.assertFalse(self.eu.check_password(username, weak_pw_length))

        # Weak password doesn't meet character requirements
        self.assertFalse(self.eu.check_password(username, weak_pw_condition))

        # Weak password is part of the invalid password list
        self.assertFalse(self.eu.check_password(username, weak_pw_weak_lst))

    @patch("builtins.input", side_effect=["jason", "Test@1234", "2"])
    def test_valid_registration(self, side_effect):
        """
        Integration test using the register() UI to test user inputs and ensure that registration is successful
        """
        self.eu.register()
        with open(self.eu.pw_manager.filepath, "r") as file:
            users = file.readlines()

        user_info = users[0].strip().split(", ")

        # Checks username input is same as stored in Password file
        self.assertEqual("jason", user_info[0])

        # Checks password input is same as stored in Password file when unhashed
        self.assertTrue(bcrypt.checkpw("Test@1234".encode('utf-8'), user_info[1].encode('utf-8')))

        # Checks role is same as stored in Password file
        self.assertEqual(RolesEnum.PREMIUM_CLIENT.value, user_info[2])


if __name__ == '__main__':
    unittest.main()