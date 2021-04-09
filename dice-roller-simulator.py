import random

def play_again():
    again = input('Do you want to roll the dice again? (Y/N): ').upper()
    if again == "Y":
        roll()
    elif again == "N":
        print("Thank your for playing.")
    else:
        print("Wrong input! Enter again.")
        play_again()

def roll():
    dice_no = random.randint(1, 6)
    print( "The dice number is", dice_no )
    play_again()

print("Welcome to dice roller simulator!")
roll()