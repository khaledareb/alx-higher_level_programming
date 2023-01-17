class Dog:
    #defined attributes of the object that will be given name later under the class DOG
    #feilds also named variable are the attributes
    def __init__(self, name="", height=0, weight =0):
        self.name = name
        self.height = height
        self.weight = weight
    ##attribute of the object dog defined


    #capabailites to be defined now (Methods/functions)

    def run(self):
        print("{} the dog runs".format(self.name))
def main():
    spot = Dog("Spot" , 66, 26)


    spot.run()
    bowser = Dog()
    bowser.run()
main()






