class User:
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\nUser info:\nFirst name: {self.f_name}\n"
              f"Last name: {self.l_name}\n"
              f"Age: {self.age}")

    def greet_user(self):
        print(f"\nHello {self.f_name} {self.l_name}!")

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

admin = Admin("admin", "admin", 35)
admin.privileges.show_privileges()