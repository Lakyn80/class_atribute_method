class Car:
    def __init__(self, color, model):
        self.color = color  # Use the color passed when creating the object
        self.model = model  # Use the model passed when creating the object

    def describe_car(self):
        print(f"The car is {self.color} and the model is {self.model}")

# Creating two different cars
car1 = Car("red", "Ferrari")
car2 = Car("blue", "Volkswagen")

# Calling the describe_car method for both cars
car1.describe_car()  # Output: The car is red and the model is Ferrari
car2.describe_car()  # Output: The car is blue and the model is Volkswagen
