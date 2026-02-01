def factor(num = int(input("Give me a number to factor"))):
    for i in range(1, num + 1):
            if num % i == 0:
                print(i)
    num = int(input())
factor() 