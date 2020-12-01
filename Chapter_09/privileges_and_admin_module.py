from user_module import User
class Privileges:
    def __init__(self):
        self.privileges_list = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges_list:
            print(privilege.title())

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()