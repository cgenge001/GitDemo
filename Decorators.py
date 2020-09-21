import time as t
import math

def TotExecution_Time(func):
    def inner(n):
        starttime= t.time()
        func(num)
        endtime = t.time()
        print("The total execution time taken:",endtime-starttime)
    return inner

@TotExecution_Time
def Factorial(n):

    fact = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           t.sleep(1)
           fact = fact*i
       print("The factorial of",num,"is",fact)

# To take input from the user
num = int(input("Enter a number: "))
t.sleep(3)
Factorial(num)