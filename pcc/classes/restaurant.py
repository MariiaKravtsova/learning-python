class Restaurant():
    """Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, ' is opened.')

my_restaurant = Restaurant('Studio Grill', 'American')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
