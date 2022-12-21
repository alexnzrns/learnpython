class Restaurant():
    offen = bool
    offen = False
    
    def __init__(self, name, cusinetype, seats):
        self.name = name
        self.cusinetype = cusinetype
        self.seats = seats

    def describe_restaurant(self):
        print("Name: ", self.name)
        print("Küche: ", self.cusinetype)
        print("Sitzplätze: ", self.seats)
        print("Geöffnet? ", self.offen)
    
    def openrestaurant(self):
        self.offen = True
    
    def closerestaurant(self):
        self.offen = False



class Eisdiele(Restaurant):
    def __init__(self, name, cuisinetype, seats, sorten):
        super().__init__(self, name, cuisinetype,  seats)
        self.sorten = sorten
    
    def describe_eisdiele(self):
        print("Name: ", self.name)
        print("Küche: ", self.cusinetype)
        print("Sitzplätze: ", self.seats)
        print("Eissorten: ", self.sorten)

r1 = Restaurant("Bla", "ital.", 233)
r1.openrestaurant()
r1.describe_restaurant()   
e1 = Eisdiele("My", "arab", 20, "Schoko, Vanille, Himmelblau")
e1.openrestaurant()
e1.describe_eisdiele()     