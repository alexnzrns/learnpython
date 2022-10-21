class User():
    def __init__(self, firstname, lastname, gender):
        self._firstname = firstname
        self._lastname = lastname
        self._gender = gender

    def describe_user(self):
        vorname = self._firstname
        nachname = self._lastname
        geschlecht = self._gender
        ausgabe = print(
        "Vorname: " + vorname +
        "\nNachname: " + nachname + 
        "\nGeschlecht: " + geschlecht
        )
        return ausgabe

    def greet_user(self):
        if self._gender == "m":
            ausgabe = print("Hallo Herr " + self._lastname + ", wie geht es Ihnen?")
        elif self._gender == "w":
            ausgabe = print("Hallo Frau " + self._lastname + ", wie geht es Ihnen?")
        else:
            ausgabe = print("Hallo " + self._firstname + " " + self._lastname)

        return ausgabe

p1 = User("Alex", "Nazarenus", "m")
p1.describe_user()
p1.greet_user()

p2 = User("Pipo", "Müller", "d")
p2.describe_user()
p2.greet_user()

p3 = User("Peter", "Vater", "m")
p3.describe_user()
p3.greet_user()

p4 = User("Angela", "Merkel", "w")
p4.describe_user()
p4.greet_user()