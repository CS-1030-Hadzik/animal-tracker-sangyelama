class Animal:
    """
    Base class representing a generic animal.
    """

    # Class-level attribute
    kingdom = "Animalia"

    # Class-level list to store all Animal objects
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)

    def speak(self):
        return "The animal makes a noise."

    def __str__(self):
        return f"Kingdom: {self.kingdom}, Name: {self.name}, Species: {self.species}"
