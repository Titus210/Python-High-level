class Square:
    
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    
    @property
    def height(self):
        print("Retrieving the height....")
        
        return self.__height
    
    @height.setter
    def height(self, value):
        # value.isdigit():
        self.__height = value
        
        #else:
        #    print("Only integers allowed")
            
    
    @property
    def width(self):
        print("Retrieving the width....")

        return self.__width

    @width.setter
    def width(self, value):
       # if value.isdigit():
        self.__width = value

      #  else:
      #      print("Only integers allowed")

    
    def get_area(self):
        return int(self.__width) * int(self.__height)
    

def main():
    a_square = Square()
    
    height = input('Enter a height: ')
    width = input('Enter a width: ')
    
    
    a_square.height = height
    a_square.width = width
    
    print(f"Height: {a_square.height}")
    print(f"Width:  {a_square.width}")
    
    print(f"Area:  {a_square.get_area()}")
    
main()