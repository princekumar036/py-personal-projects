import random

def roll_again():
    again = input('Do you want to roll the dice again? (Y/N): ').upper()
    if again == "Y":
        roll()
    elif again == "N":
        print("Thank your for playing.")
    else:
        print("Wrong input! Enter again.")
        roll_again()

def roll():
    dice_no = random.randint(1, 6)
    print( "The dice number is", dice_no )
    roll_again()

print("Welcome to dice roller simulator!")
roll()