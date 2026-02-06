'''Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ".'''
import math
bill = 100

tip_amount = int(input("Your subtotal is 100. How much would you like to tip."))
def tip_quality():
    print(f"Your total amount is {100+tip_amount}")
    if tip_amount <= 0:
        print("BAD tip")
    elif tip_amount <= 15:
        print("okay tip")
    elif tip_amount <= 20:
        print("Good Tip")
    elif tip_amount <= 25:
        print("Great Tip")
tip_quality()