def factor(x):
    for i in(1,x+1):
        if x % i == 0:
            print(i)
x= int(input(""))
factor(x)