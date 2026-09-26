from enum import Enum

class UserRole(str,Enum):
    EMPLOYEE = "employee"
    HR_EXECUTIVE = "hr_executive"
    HR_MANAGER = "hr_manager"
    ADMIN = "admin"