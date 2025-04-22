
from animal import Animal
from dog import Dog

if __name__ == "__main__":
    # Create an instance of the Animal class
    animal1 = Animal("Simba", "Lion")

    # Print the Animal instance
    print(animal1)

    # Call the method to make a generic animal sound
    print(animal1.speak())

    # Create an instance of the Dog class
    dog1 = Dog("Max", "Canine", "Labrador")

    # Print the Dog instance
    print(dog1)

    # Call the method to make the dog-specific sound
    print(dog1.speak())

    # Print out all the animals
    print("\nAll Animals:")
    for animal in Animal.all_animals:
        print(animal)

