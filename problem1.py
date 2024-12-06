from enum import Enum
import time

class RolesEnum(Enum):
    """
    The Roles that are accessible for the justInvest app
    """
    CLIENT = "Client"
    PREMIUM_CLIENT = "Premium Client"
    FINANCIAL_PLANNER = "Financial Planner"
    FINANCIAL_ADVISOR = "Financial Advisor"
    TELLER = "Teller"

class TasksEnum(Enum):
    """
    The Tasks that are allowed given appropriate permission for the justInvest app
    """
    ACCOUNT_BALANCE = "account balance"
    INVESTMENT_PORTFOLIO = "investment portfolio"
    ADVISOR_CONTACT = "advisor contact details"
    PLANNER_CONTACT = "planner contact details"
    MONEY_MARKET_INSTRUMENTS = "money market instruments"
    PRIVATE_CONSUMER_INSTRUMENTS = "private consumer instruments"

class PermissionsEnum(Enum):
    """
    The permissions that certain roles have based on their tasks for the justInvest app
    """
    READ = "View"
    WRITE = "Modify"

class AccessControlMechanism:
    """
    The AccessControlMechanism implements an RBAC, distinguishes the enrolled user's permissions and allows them to perform only their authorized operations
    """
    def __init__(self) -> None:
        self.roles_permissions: dict[list] = {}
        self.business_hours: bool = False
    
    def set_business_hours(self, hours: bool) -> None:
        """Sets True during hours of operations, False if outside hours of operatoins of the justInvest app """
        self.business_hours = hours
    
    def define_role_permissions(self) -> dict[list]:
        """Returns a dictionary with keys representing the roles, and the values are a list of tuples containing the role's tasks and their permissions"""
        self.roles_permissions = {
            RolesEnum.CLIENT: [(PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), (PermissionsEnum.READ, TasksEnum.INVESTMENT_PORTFOLIO), (PermissionsEnum.READ, TasksEnum.ADVISOR_CONTACT)], 
            RolesEnum.PREMIUM_CLIENT: [(PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), (PermissionsEnum.READ, TasksEnum.INVESTMENT_PORTFOLIO), (PermissionsEnum.WRITE, TasksEnum.INVESTMENT_PORTFOLIO), (PermissionsEnum.READ, TasksEnum.ADVISOR_CONTACT)],
            RolesEnum.FINANCIAL_ADVISOR: [(PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), (PermissionsEnum.READ, TasksEnum.INVESTMENT_PORTFOLIO), (PermissionsEnum.READ, TasksEnum.PRIVATE_CONSUMER_INSTRUMENTS)],
            RolesEnum.FINANCIAL_PLANNER: [(PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), (PermissionsEnum.READ, TasksEnum.INVESTMENT_PORTFOLIO), (PermissionsEnum.READ, TasksEnum.MONEY_MARKET_INSTRUMENTS), (PermissionsEnum.READ, TasksEnum.PRIVATE_CONSUMER_INSTRUMENTS)],
            RolesEnum.TELLER: [(PermissionsEnum.READ, TasksEnum.ACCOUNT_BALANCE), (PermissionsEnum.READ, TasksEnum.INVESTMENT_PORTFOLIO)]
        }

    def get_permissions(self, role: str) -> list:
        """
        Returns a list of the role's task and respective permission as a list of tuples
        """
        return self.roles_permissions[RolesEnum(role)]
        
    def get_operations(self, role: str) -> list[str]:
        """
        Returns a list of strings that representing the numerical value of the operation or X to logout for a specific role
        """
        operations_lst = []
        if role == RolesEnum.TELLER.value and not self.business_hours:
            return ["X"]
        permissions = self.get_permissions(role)
        for permission in permissions:
            match permission[1]:
                case TasksEnum.ACCOUNT_BALANCE:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("1")
                case TasksEnum.INVESTMENT_PORTFOLIO:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("2")
                        case PermissionsEnum.WRITE:
                            operations_lst.append("3")
                case TasksEnum.ADVISOR_CONTACT:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("4")
                case TasksEnum.PLANNER_CONTACT:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("5")
                case TasksEnum.MONEY_MARKET_INSTRUMENTS:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("6")
                case TasksEnum.PRIVATE_CONSUMER_INSTRUMENTS:
                    match permission[0]:
                        case PermissionsEnum.READ:
                            operations_lst.append("7")
        operations_lst.append("X")
        return operations_lst

    def print_operations(self, role: str):
        """
        Prints the list of operations available to the role
        """
        operations = self.get_operations(role)
        if operations:
            print("Your authorized operations are:")
            print(", ".join(operations))
        if role == RolesEnum.TELLER.value and not self.business_hours:
            print("""
Cannot access authorized operations outside of business hours.
Please try again from 9:00am to 5:00pm.
""")
            
    def perform_operation(self, role: str, operation: str) -> bool:
        """
        Prints out the selected operation, given the authroized operations of a role
        """
        operations_lst = self.get_operations(role)
        if operation not in operations_lst:
            print("Invalid operation, Please try again.")
            return False
        match operation:
            case "1":
                print("Viewing account balance...")
            case "2":
                print("Viewing investment portfolio...")
            case "3":
                print("Modifying investment portfolio...")
            case "4":
                print("Viewing Financial Advisor contact info...")
            case "5":
                print("Viewing Financial Planner contact info...")
            case "6":
                print("Viewing Money Market Instruments...")      
            case "7":
                print("Viewing Private Consumer Instruments...")
            case "X":
                print("Logging out...")
                return False
        for i in range(10):  
            print(".")
            time.sleep(0.2)
        print("Operation Complete.")
        return True