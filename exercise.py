'''under 12,greater than 65,resident,member'''
def special_services():
    age = int(input("What is your age?"))
    if age < 12:
        print("You get a discount")
    elif age >= 65:
        print("You get a discount")
    else:
        member = input("You have a member card")
        if member == "True" or "Yes" or "yes":
            print("You get a discount")
        else:
            resident = input("Do you live around here")
            if resident == "True" or "Yes" or "yes":
                print("You get a discount")


    
special_services()