bill = 100
tip_amount = int(input("What amount of money would you like to tip. Your subtotal is 100 dollars" ))
def tip_quality():
    print("Your total is ", 100 + tip_amount)
    if tip_amount <= 0:
        print("Bad Tip just like the kind of person the tipper is.")
    elif 1 < tip_amount <= 15:
        print("Okay Tip")
    elif tip_amount <= 20:
        print("Good Tip")
    else:
        print("Great Tip")
tip_quality()
