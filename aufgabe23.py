class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, seats):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__seats = seats

    def describe_restaurant(self):
        print("Restaurant Name: ", self.__restaurant_name)
        print("Cusine Type: ", self.__cuisine_type)
        print("Anzahl Plätze: ", self.__seats)

    def open_restaurant():
        pass
