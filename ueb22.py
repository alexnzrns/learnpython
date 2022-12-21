class Queue():
    warteschlange = []
    
    def __init__(self):
        pass
    def ankommen(self, user):
        self.warteschlange.append(user)
    def verlassen(self, user):
        self.warteschlange.remove(user)
    def anzahl(self):
        print("Länge der Warteschlange: ", len(self.warteschlange))
    def ausgabe(self):
        for i in self.warteschlange:
            print("Hallo ", i)


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

q1 = Queue()
q1.ankommen(u1)
q1.ausgabe()
q1.anzahl()
q1.verlassen(u1)
q1.anzahl()