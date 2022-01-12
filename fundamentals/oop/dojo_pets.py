
    
    
class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 55
        return self
    
    def noise(self):
        print("WOOF WOOF")
        return self
    
    
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    
    def pet_stats(self):
        print(f"Health: {self.pet.health}, Energy: {self.pet.energy}")
        return self

my_treats = ["Bacon", "Bones", "Pizza"]
my_pet_food = ["Dr. Gary's Best Breed", "Treats"]

cal = Pet("Caliber", "German Shepherd",["Laser Dog", "Squirrel hunter"])
nolan = Ninja("Nolan","Rangel", my_treats, my_pet_food, cal)

nolan.walk().walk().bathe().pet_stats()