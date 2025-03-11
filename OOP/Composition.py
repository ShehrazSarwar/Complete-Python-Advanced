# Composition = Dependant relationship

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def charge(self):
        return "Battery is charging!"

class Laptop:
    def __init__(self, brand, battery_capacity):
        self.brand = brand
        self.battery = Battery(battery_capacity)  # Composition (battery is part of Laptop)

    def show_details(self):
        return f"Laptop: {self.brand}, Battery: {self.battery.capacity}mAh"

# Creating a Laptop object
laptop1 = Laptop("Dell", 5000)

print(laptop1.show_details())  # Output: Laptop: Dell, Battery: 5000mAh
print(laptop1.battery.charge())  # Output: Battery is charging!
