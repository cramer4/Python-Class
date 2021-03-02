class Employee:
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def raise_salary(self, money=""):
        if money:
            self.salary += money
        else:
            self.salary += 5000
        print(self.salary)


jj = Employee("jordan", "jamsey", 5000)
jj.raise_salary()
