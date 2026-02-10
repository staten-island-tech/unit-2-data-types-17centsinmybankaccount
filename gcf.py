def gcf():
    def factor(num = int(input("give me an number to factor"))):
        for i in range(1,num+1):
            if num % i == 0:
                print(i)
        factor()
    