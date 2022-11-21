# Erstellt die VwPkw Oberklasse
class VwPkw:
    # Alle erbenen Klassen haben folgende Eigenschafen wenn sie nicht geändert werden
    owner = "Company"
    name = "Car"
    weight = -1
    ps = -1
    wheels = 4

    # Der Owner muss angegeben werden zum erstellen eines neuen PKWs
    def __init__(self, owner):
        self.owner = owner

    # Auch die Funktionen werden vererbt
    def print_owner(self):
        print("This PKW belongs to " + self.owner)

    def drive(self):
        print("OMG " + self.name + " by " + self.owner + " starts driving!!")


# Erstellt eine Unterklasse, namens VwPolo die von VwPkw erbt
class VwPolo(VwPkw):
    # Überschreibt den Namen
    name = "VW Polo"

    # Erbt die Eigenschafen der Oberklasse, die entsteht bei den angegeben Parametern
    def __init__(self, owner):
        super().__init__(owner)


# Erstellt eine Unterklasse, namens VwGolf die von VwPkw erbt
class VwGolf(VwPkw):
    # Überschreibt den Namen
    name = "VW Golf"

    # Erbt die Eigenschafen der Oberklasse, die entsteht bei den angegeben Parametern
    def __init__(self, owner):
        super().__init__(owner)


# Erstellt eine Unterklasse, namens VwCabrio die von VwPkw erbt
class VwCabrio(VwPkw):
    # Überschreibt den Namen
    name = "VW Kabrio"

    # Erbt die Eigenschafen der Oberklasse, die entsteht bei den angegeben Parametern
    def __init__(self, owner):
        super().__init__(owner)

    # Eine Funktion die nur das Cabrio besitzt
    def open_roof(self):
        print(self.name + " by " + self.owner + " opens it's roof")


# Erstellt eine neue Instanz des Cabrios mit dem Owner "Ich"
cabrio = VwCabrio("Ich")

# Ruft Funktionen auf
cabrio.open_roof()
cabrio.drive()