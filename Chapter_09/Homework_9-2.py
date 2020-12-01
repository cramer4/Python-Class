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
le_crave = Restaurant("Le Crave", "French")
franciscos = Restaurant("Francisco's Mexican Restaurant", "Mexican")

restaurants = [jimmys_bbq, le_crave, franciscos]
for restaurant in restaurants:
    restaurant.describe_restaurant()