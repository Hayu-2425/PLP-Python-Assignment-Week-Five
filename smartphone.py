# Smartphone base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"🔋 Battery charged. Current level: {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}% battery."

# Inheritance: GamingPhone extends Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system!")
            self.battery -= 10
        else:
            print("⚠️ Battery too low to play games!")

# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 256, 80)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 512, 90, "liquid-cooling")

print(phone1)  
phone1.call("123-456-789")
phone1.charge(15)

print("\n" + str(gaming_phone))
gaming_phone.play_game("PUBG")
gaming_phone.charge(5)
