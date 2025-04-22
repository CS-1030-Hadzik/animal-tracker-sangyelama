from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species, breed):
        super().__init__(name, species)  # Initialize name and species from Animal
        self.breed = breed  # Dog-specific attribute

    def __str__(self):
        return f"Kingdom: {self.kingdom}, Name: {self.name}, Species: {self.species}, Breed: {self.breed}"

    def speak(self):
        return "The dog barks."
