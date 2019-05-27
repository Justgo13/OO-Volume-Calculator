class Shape(object):
    length = 0
    width = 0
    height = 0
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def cube_volume(self):
        return self.length**3

    def pyramid_volume(self):
        return (self.length*self.width*self.height)/3

        
    def triangle_pyramid_volume(self):
        return 1/3*(self.length*self.width*self.height)

choice = input("Type 'cube' to find volume of cube, type 'pyramid' to find volume of " +
               "square based pyramid, type'tri pyramid' to find volume of triangle based " +
               "pyramid and type 'quit' to quit: ")

if choice == 'cube':
    length = float(input("Enter a length: "))
    obj = Shape(length,length,length)
    print("Your cube volume is {}".format(obj.cube_volume()))
elif choice  == 'pyramid':
    length = float(input("Enter a length: "))
    width = float(input("Enter a width: "))
    height = float(input("Enter a height: "))
    obj = Shape(length,width,height)
    print("Your square based pyramid volume is {}".format(obj.pyramid_volume()))
elif choice == 'tri pyramid':
    length = float(input("Enter a length: "))
    width = float(input("Enter a width: "))
    height = float(input("Enter a height: "))
    obj = Shape(length,width,height)
    print("Your triangle based pyramid volume is {}".format(obj.triangle_pyramid_volume()))
else:
    print("Thanks for using our application")
    quit()
