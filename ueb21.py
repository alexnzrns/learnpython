class User():
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
    
    def describe_user(self):
        print("Vorname: ", self.firstname)
        print("Nachname: ", self.lastname)
        print("Geschlecht: ", self.gender)

    def greet_user(self):
        if self.gender == "m":
            print("Sehr geehrter Herr ", self.lastname, " \nschön Sie zu sehen!")
        elif self.gender == "w":
            print("Sehr geehrte Frau ", self.lastname, " \nschön Sie zu sehen!")
        else:
            print("Sehr geehrtes Etwas, moin.")

u1 = User("Alexander", "Nazarenus", "m")
u1.describe_user()
u1.greet_user()
u2 = User("Pipo", "Müller", "w")
u2.describe_user()
u2.greet_user()
u3 = User("Josch", "Böhm", "d")
u3.describe_user()
u3.greet_user()