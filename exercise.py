'''under 12,greater than 65,resident,member'''
def special_services():
    age = int(input("What is your age?"))
    if age < 12:
        print("You get a discount")
    elif age >= 65:
        print("You get a discount")
    else:
        member = input("You have a member card")
        uppercase_member = member.upper()
        if uppercase_member == "YES":
            print("You get a discount")
        else:
            resident = input("Do you live around here")
            uppercase_resident = resident.upper()
            if uppercase_resident == "YES":
                print("You get a discount")
            else:
                print("No Discount")


    
special_services()                      