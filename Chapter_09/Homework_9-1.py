class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cusine = cuisine
        self.open = True

    def describe_restaurant(self):
        print(f"{self.name} is a {self.cusine} restaurant.")

    def open_restaurant(self):
        if self.open == True:
            print(f"{self.name} is open!")
        else:
            print(f"{self.name} is closed.")

jimmys_bbq = Restaurant("Jimmy's barbecue", "barbecue")

jimmys_bbq.open_restaurant()
jimmys_bbq.describe_restaurant()