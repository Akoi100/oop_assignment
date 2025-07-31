##Assignment 1: Design Your Own Class! 
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def display_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}"

class IOSSmartphone(Smartphone):
    def __init__(self, brand, model, storage, ios_version):
        super().__init__(brand, model, storage)
        self.ios_version = ios_version

    def display_info(self):
        return f"{super().display_info()} and iOS version {self.ios_version}"

# Example usage
smartphone = Smartphone("GenericBrand", "ModelX", 128)
ios_smartphone = IOSSmartphone("Apple", "iPhone 13", 256, "15.0")

print(smartphone.display_info())
print(smartphone.make_call("123-456-7890"))
print(ios_smartphone.display_info())
print(ios_smartphone.make_call("098-765-4321"))



#Activity 2: Polymorphism Challenge! 🎭
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

# Example usage
def vehicle_movement(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()
boat = Boat()

vehicle_movement(car)
vehicle_movement(plane)
vehicle_movement(boat)
