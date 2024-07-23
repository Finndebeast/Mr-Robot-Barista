# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:23:32 2024

@author: Finn de Boer
"""
import sys


print("Hello and welcome to Finn's coffee shop!")


name = input("What's your name?\n")


menu = "\nBlack Coffee\n" + "Tea\n" + "Latte\n" + "Cappuccino"


if name == "Tijn" or name == "Twan":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("\nYOU ARE NOT WELCOME HERE EVIL " + name + "! " + "GET OUT!")
        sys.exit()
    else:
        print("\nHello " + name + ", what do you want to order? Here's the menu.\n" + menu)
else: 
    print("\nHello " + name + ", what do you want to order? Here's the menu.\n" + menu)


order = input()


p_black_coffee = 5 


p_tea = 3


p_latte = 7 


p_cappuccino = 6


if order == "Black Coffee":
    product = p_black_coffee
elif order == "Tea":
    product = p_tea
elif order == "Cappuccino":
    product = p_cappuccino 
elif order == "Latte":
    product = p_latte
else: 
    print("\nSorry, we don't have that here.")
    sys.exit(1)


amount = int(input("\nHow many cups of " + order + " would you like?\n"))


price = product * amount


pay = input("\nThat will be $" + str(price) + ".\nSelect the amount you'll have to pay\n")


change = int(pay) - price


if int(pay) == price:
    print("\nGreat! Your " + order + " will be done in a few moments!\n" + "Thank you for ordering at Finn's coffee shop!")     
elif int(pay) > price:
    print("\nGreat! Your " + order + " will be done in a few moments!\n" + "Here's your change: $" + str(change) + "\n"
          "Thank you for ordering at Finn's coffee shop!")  
else: 
    print("\nYou haven't given me the right amount of money! Goodbye!")


    

    
    
    


    