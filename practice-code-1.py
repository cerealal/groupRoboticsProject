#Practice Code 1
#Jacob Mealey
import sys

x = input("What's your name? ")

def stuff(thing):
    global x
    if (thing >= 14):
        print("Wow thats a thing!")
        print("wow thats a coool name,", x)
        print("Where are you from " + x , "?")
    if (x == "Jacob"):
        print("you are my leader!")
        name= x.split("a")
        print(name[1])
    else:
        sys.exit()


if __name__ == "__main__":
    stuff(41)

    
    

