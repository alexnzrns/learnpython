class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, seats):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__seats = seats

    def describe_restaurant(self):
        print("Restaurant Name: ", self.__restaurant_name)
        print("Cusine Type: ", self.__cuisine_type)
        print("Anzahl Plätze: ", self.__seats)

    def open_restaurant(self):
        return True
    
    def close_restaurant(self):
        return False

class Eisdiele(Restaurant):
   
    def __init__(self, restaurant_name, cuisine_type, seats, sorten):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__seats = seats
        self.__sorten = sorten

    def describe_eisdiele(self):
        print("Eisdielen Name: ", self.__restaurant_name)
        print("Küchen Typ: ", self.__cuisine_type)
        print("Anzahl Plätze: ", self.__seats)
        print("Sorten: ", self.__sorten)

r1 = Restaurant("Bester Grieche", "griechisch", 250)
r2 = Restaurant("Geile Deutsche Küche", "deutsch", 100)
r3 = Restaurant("Top Asiate", "asiatisch", 40)
r4 = Eisdiele("Luigis Best's", "italienisch", 10, ['schoko', 'vanille', 'erdbeere'])

#print("Restaurant ist geöffnet:", r1.open_restaurant())
print(r4.describe_eisdiele())