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

will = User("Will", "Byers", 12)
mike = User("Mike", "Wheeler", 12)
steve = User("Steve", "Harrington", 16)
users = [will, mike, steve]

for user in users:
    user.describe_user()
    user.greet_user()