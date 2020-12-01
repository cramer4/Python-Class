class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cusine = cuisine
        self.open = True
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cusine} restaurant.")

    def open_restaurant(self):
        if self.open == True:
            print(f"{self.name} is open!")
        else:
            print(f"{self.name} is closed.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self):
        self.number_served += 100

restaurant = Restaurant("restaurant", "food")
restaurant.set_number_served(5)
restaurant.increment_number_served()
print(restaurant.number_served)