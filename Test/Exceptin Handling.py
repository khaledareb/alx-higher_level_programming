class DogNameError(Exception):

    def __int__(self, *args, **kwargs):
        Exception.__int__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name : ")
    if any(char.isdigit() for char in dogName):
        raise DogNameError

except DogNameError :
    print("Your dogs name cant coytain nunber")