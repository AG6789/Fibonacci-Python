#Fibonacci Series

fList = []

def fibonacci(x):
    
    f1 = 1
    f2 = 1
    
    while len(fList) < x:
        fList.append(f1)
        fList.append(f2)
        f1 += f2
        f2 += f1
        

    
    if len(fList) >= x:
        fNumber = fList[x]
        return fNumber
    

toCheck = int(input("Which number would you like to know? "))

print(fibonacci(toCheck), fList)