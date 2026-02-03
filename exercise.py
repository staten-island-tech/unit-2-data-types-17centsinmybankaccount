'''under 12,greater than 65,resident,member'''
def special_services():
    age = int(input("What is your age?"))
    if age < 12:
        print("You get a discount")
    if age >= 65:
        print("You get a discount")
    member = bool(input("You have a member card"))
    if member == True:
        print("You get a discount")
     