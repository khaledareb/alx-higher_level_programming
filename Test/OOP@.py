class Square:
    def __int__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    #allows us to refer to indivduals feilds(attribute)

    #this is a code that gets the value of the height
    def height(self):
        print("Retreiving the height")

        return self.__height

    #to set the value of height and protect from a wrong value
    @height.setter
    def height(self, value):
       if value.isdigit():
           self.__height = value
       else:
           print("Please only enter numbers for height")


    #allows us to refer to indivduals feilds(attribute)

    #this is a code that gets the value of the height
    @property
    def width(self):
        print("Retreiving the wdith")

        return self.__width

    #to set the value of height and protect from a wrong value
    @width.setter
    def width(self, value):
       if value.isdigit():
           self.__width = value
       else:
           print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aSquare = Square()

    height = input("Enter height: ")
    width = input("Enter the width: ")

    aSquare.height = height
    aSquare.width = width

    print("Height: ", aSquare.height)
    print("Width: ", aSquare.width)

    print("The area is : ", aSquare.getArea())

main()