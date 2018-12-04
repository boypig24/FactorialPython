#the actual code:
def factorial(x):
    if x.isdigit():
        x = int(x)
        if x < 0:
            return("ERROR,input invalid")
        elif x == 0:
            return(1)
        else:
            loopAns = 1
            for loopVar in range (2,x+1):
                loopAns = loopAns*loopVar
            return(loopAns)
    else:
        return("ERROR,input invalid")

#just an example of the code's usage
def askLoop(): 
    x = input("please enter a number ")
    print(factorial(x))
    askLoop()
askLoop()
