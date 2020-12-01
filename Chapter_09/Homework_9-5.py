class User:
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser info:\nFirst name: {self.f_name}\n"
              f"Last name: {self.l_name}\n"
              f"Age: {self.age}")

    def greet_user(self):
        print(f"\nHello {self.f_name} {self.l_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts reset.")

user = User("generic", "user", "")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print(user.login_attempts)