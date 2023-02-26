# Create a class of Dog
class Dog:

    def __init__(self, name="", height=0, weight=0):
        self.height = height
        self.weight = weight
        self.name = name

    def run(self):
        """Create a method to define if dog runs"""
        
        print(f"{self.name} can run")
        ## call speed method depending on the height and weight of dog
        
        
        def dog_speed(weight, height):
            if self.weight > 50 and self .height > 20:
                speed = 20
            speed = 30
            
            return speed
        print(dog_speed(self.height, self.weight))

    def eat(self):
        """Create a method to define if dog eats"""

        print(f"{self.name} can eat")

    def bark(self):
        """Create a method to define if dog barks"""

        print(f"{self.name} barks")


def main():
    
    pops = Dog("Spot", 33, 24)
    
    pops.run()

main()