# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on water.")

# Another example: Animals
class Animal:
    def move(self):
        print("The animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("🐕 The dog is running.")

class Bird(Animal):
    def move(self):
        print("🐦 The bird is flying.")

# Example usage (polymorphism in action)
vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Bird()]

print("🚘 Vehicle Movements:")
for v in vehicles:
    v.move()

print("\n🐾 Animal Movements:")
for a in animals:
    a.move()
