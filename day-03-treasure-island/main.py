print("Welcome to the treasure island \nYour mission is to find the treasure")
choice1 = input("You're at crossroads. Where do you want to go? left or right? ")
if choice1 == "left":
     choice2 = input("swim or wait? ")
     if choice2 == "wait":
          print("you waited")

          choice3 = input("Which door? red, yellow or blue? ")

          if choice3 == "red":
           print("Burned by fire, game over")

          elif choice3 =="blue":
              print("eaten by beasts, game over")

          elif choice3 == "yellow":
              print("You Win!")  
          else:  
              print("game over")   
else:
    print("game over")
