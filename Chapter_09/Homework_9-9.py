class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 260

        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        self.battery_size = 100

class Electric_car(Car):
    def __init__(self, make, model, year):
        super(Electric_car, self).__init__(make, model, year)
        self.battery = Battery()

my_tesla = Electric_car("tesla", "model s", 2019)
my_tesla.battery.get_range()


my_tesla.battery.upgrade_battery()
print("\nUpgrading battery!\n")
my_tesla.battery.get_range()