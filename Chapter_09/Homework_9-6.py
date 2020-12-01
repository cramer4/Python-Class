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

class Ice_cream_stand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())

ice_cream_stand = Ice_cream_stand("Ice cream stand", "Ice cream")
ice_cream_stand.display_flavors()