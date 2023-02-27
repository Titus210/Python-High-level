import math

# create class python

class Circle:
    def __init__(self,val, props ='r'):
        if props == 'r': #radius
            self.radius = val
            
        elif props == 'd': # diameter
            self.radius = val / 2
            
        elif props == 'c': #circumference
            self.radius = val * (math.pi)
            
        elif props == "a":
            self.radius = (val / math.pi) ** .5
            
        else:
            raise  Exception("Prop must be r, d, c, a")
        
        self.diameter = self.radius * 2
        self.circumference = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi
        

        