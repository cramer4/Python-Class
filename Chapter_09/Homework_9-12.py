from user_module import User
from privileges_and_admin_module import Privileges, Admin

admin = Admin("admin", "admin", 35)
admin.privileges.show_privileges()