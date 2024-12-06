import unittest
from problem1 import *

class problem1_test(unittest.TestCase):

    def setUp(self):
        """
        Setup the Access Control Mechanism and initializes the role permissions
        """
        self.ac = AccessControlMechanism()
        self.ac.define_role_permissions()
    
    def test_roles_enum(self):
        """
        Unit tests for the RolesEnum enum
        """
        self.assertEqual("Client", RolesEnum.CLIENT.value)
        self.assertEqual("Premium Client", RolesEnum.PREMIUM_CLIENT.value)
        self.assertNotEqual(RolesEnum.FINANCIAL_ADVISOR.value, RolesEnum.FINANCIAL_PLANNER.value)

    def test_tasks_enum(self):
        """
        Unit tests for the TasksEnum enum
        """
        self.assertEqual("account balance", TasksEnum.ACCOUNT_BALANCE.value)
        self.assertEqual("investment portfolio", TasksEnum.INVESTMENT_PORTFOLIO.value)
        self.assertNotEqual(TasksEnum.MONEY_MARKET_INSTRUMENTS.value, TasksEnum.PLANNER_CONTACT.value)

    def test_permissions_enum(self):
        """
        Unit tests for the PermissionsEnum enum
        """
        self.assertEqual("View", PermissionsEnum.READ.value)
        self.assertEqual("Modify", PermissionsEnum.WRITE.value)
    
    def test_set_business_hours(self):
        """
        Unit tests for the set_business_hours() function
        """
        self.ac.set_business_hours(True)
        self.assertTrue(self.ac.business_hours)

        self.ac.set_business_hours(False)
        self.assertFalse(self.ac.business_hours)

    def test_define_role_permissions(self):
        """
        Unit tests for the define_role_permissions() function
        """
        role_permissions = self.ac.roles_permissions
        self.assertIn(RolesEnum.CLIENT, role_permissions)
        self.assertIn((PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), role_permissions[RolesEnum.CLIENT])

        self.assertNotIn("Manager", role_permissions)

    def test_get_permissions(self):
        """
        Unit tests for the get_permissions() function
        """
        client_permissions = self.ac.get_permissions("Client")
        self.assertEqual(client_permissions, self.ac.roles_permissions[RolesEnum("Client")])

        self.assertNotEqual(client_permissions, self.ac.roles_permissions[RolesEnum("Teller")])

    def test_get_operations(self):
        """
        Unit and Integration tests for the get_operations() function, including various conditions such as
        the Teller during business/non-business hours
        """
        # Operations for Teller out of business hours
        self.ac.set_business_hours(False)
        operations = self.ac.get_operations(RolesEnum.TELLER.value)
        self.assertEqual(["X"], operations)  

        # Operations for Teller during business hours
        self.ac.set_business_hours(True)
        operations = self.ac.get_operations(RolesEnum.TELLER.value)
        self.assertEqual(["1", "2", "X"], operations)

        # Operations for Client during business hours vs. non business hours
        self.ac.set_business_hours(True)
        operations_business = self.ac.get_operations(RolesEnum.CLIENT.value)
        self.ac.set_business_hours(False)
        operations_not_business = self.ac.get_operations(RolesEnum.CLIENT.value)
        self.assertEqual(operations_business, operations_not_business)

    def test_perform_operation(self):
        """
        Unit tests for the perform_operation() function
        """
        # Performs valid operation for the role
        valid_operation = self.ac.perform_operation(RolesEnum.PREMIUM_CLIENT.value, "3")
        self.assertTrue(valid_operation)

        # Performs invalid operation for the role
        invalid_operation = self.ac.perform_operation(RolesEnum.PREMIUM_CLIENT.value, "7")
        self.assertFalse(invalid_operation)

        # Performs Logout
        logout_operation = self.ac.perform_operation(RolesEnum.FINANCIAL_PLANNER.value, "X")
        self.assertFalse(logout_operation)

if __name__ == '__main__':
    unittest.main()

    
    
